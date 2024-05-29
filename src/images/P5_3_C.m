clc; clear all;

% Definir la función de transferencia
num = 1;
den = [1 4 3 0]; % Denominador del sistema
G = tf(num, den);

% Encontrar el factor de amortiguamiento para un sobreimpulso del 5%
desired_OS = 5; % Porcentaje de sobreimpulso
desired_zeta = fzero(@(z) 100 * exp(-pi * z / sqrt(1 - z^2)) - desired_OS, [0, 1]);

disp(['Factor de amortiguamiento deseado: ', num2str(desired_zeta)]);

% Encontrar el valor de K correspondiente a este factor de amortiguamiento
% Utilizaremos la aproximación de segundo orden para encontrar K
omega_n = 1; % Frecuencia natural arbitraria para la aproximación

% Resolver para K usando el polinomio característico de lazo cerrado
syms s K
polinomio_caracteristico = s^3 + 4*s^2 + 3*s + K;
polo_dominante = -desired_zeta * omega_n + 1i * omega_n * sqrt(1 - desired_zeta^2);
polo_dominante_conjugado = -desired_zeta * omega_n - 1i * omega_n * sqrt(1 - desired_zeta^2);

% Encontrar K mediante sustitución de polos dominantes en el polinomio característico
K_solution = vpasolve(polinomio_caracteristico == 0, K, 'Random', true);

% Seleccionar el valor de K positivo y más cercano al real
K_critico = double(K_solution(real(K_solution) > 0));

disp(['Valor de K para un sobreimpulso del 5%: ', num2str(K_critico)]);

% Crear la función de transferencia en lazo cerrado con K_critico
G_cl = feedback(K_critico * G, 1);

% Calcular el tiempo de estabilización
step_info = stepinfo(G_cl);
Ts = step_info.SettlingTime;

% Mostrar la información del tiempo de estabilización
disp(['Tiempo de estabilización (Ts): ', num2str(Ts), ' segundos']);

% Simular la respuesta al escalón unitario del sistema en lazo cerrado
figure;
step(G_cl);
title(['Respuesta al escalón unitario con K = ', num2str(K_critico)]);
grid on;
