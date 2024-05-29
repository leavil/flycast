clc; clear all;

% Definir la función de transferencia
num = 1;
den = [1 4 3 0]; % Denominador del sistema
G = tf(num, den);

% Trazar el lugar de raíces
figure;
rlocus(G);
sgrid;

% Encontrar el valor de K para el cual el sistema tiene polos puramente imaginarios
[k_values, poles] = rlocfind(G);

% Mostrar los polos encontrados y el valor de K correspondiente
disp(['Valor de K para polos puramente imaginarios: ', num2str(k_values)]);
disp('Polos correspondientes:');
disp(poles);

% Calcular el período de la oscilación
omega_n = abs(imag(poles(1))); % Frecuencia natural
T = 2 * pi / omega_n; % Período de oscilación

% Mostrar el período de la oscilación
disp(['Período de la oscilación: ', num2str(T), ' segundos']);

% Crear la función de transferencia en lazo cerrado con el valor crítico de K
G_cl = feedback(k_values * G, 1);

% Simular la respuesta al escalón unitario del sistema en lazo cerrado
figure;
step(G_cl);
title(['Respuesta al escalón unitario con K = ', num2str(k_values)]);
grid on;

