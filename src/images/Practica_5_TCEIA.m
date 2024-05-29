clc; clear all;

% Definir la función de transferencia
num = 1;
den = [1 4 3 0]; % Denominador del sistema
G = tf(num, den);

% Trazar el lugar de raíces
k = 0:0.001:20;
[ps, ks] = rlocus(G, k);
rlocus(G, k)
sgrid

% Buscar las posiciones donde ks es igual a 0.3
% Nota: eps es demasiado pequeño para comparar flotantes de esta magnitud
posiciones = find(abs(ks - 0.3) < 1e-3);

% Mostrar las posiciones
disp('Las posiciones donde K es igual a 0.3 son:');
disp(posiciones);

% Obtener los valores correspondientes en ps para las posiciones encontradas
valores_ps = ps(:, posiciones);

% Mostrar los valores correspondientes en ps para cada posición
disp('Los valores correspondientes en polos son:');
disp(valores_ps);

title('Lugar de Raíces de G(s)');
xlabel('Parte Real');
ylabel('Parte Imaginaria');
grid on;

% Definir los polos encontrados
polos_encontrados = valores_ps;

% Crear la nueva función de transferencia a partir de los polos encontrados
G_nueva = zpk([], polos_encontrados, 0.3); % Ganancia de 0.3

% Mostrar la nueva función de transferencia
disp('La nueva función de transferencia es:');
disp(G_nueva);

% Obtener los polos de la nueva función de transferencia
polos = pole(G_nueva);

% Calcular el factor de amortiguamiento (zeta) para cada polo
zetas = -real(polos) ./ abs(polos);

% Calcular el sobreimpulso (en porcentaje) para la respuesta al escalón unitario
step_info = stepinfo(G_nueva);
overshoot = step_info.Overshoot;

% Mostrar la información
disp('Factor de amortiguamiento para cada polo:');
disp(zetas);
disp(['Sobreimpulso (%): ', num2str(overshoot)]);

% Calcular duración del régimen transitorio del sistema
frecuencia_natural = abs(polos(1)); % Frecuencia natural omega_n
Ts1 = 4 / (zetas(1) * frecuencia_natural); % Tiempo de establecimiento aproximado (4/ζω_n)
disp('Duración del régimen transitorio del sistema:');
disp(Ts1);

% Calcular la respuesta al escalón unitario del sistema
step_info = stepinfo(G_nueva);

% Obtener el tiempo de establecimiento (settling time)
Ts = step_info.SettlingTime;

% Calcular el error en estado estable para una entrada de tipo rampa con pendiente de 0.1 unidades
% Para sistemas de tipo 0, el error en estado estable para una entrada rampa es infinito.
% Para sistemas de tipo 1, se puede calcular de manera diferente.
rampa_slope = 0.1;
ess_rampa = inf; % Asumiendo sistema de tipo 0, el error en estado estable para una rampa es infinito

% Mostrar el resultado
disp(['Error en estado estable para una entrada de tipo rampa con pendiente de 0.1 unidades: ', num2str(ess_rampa)]);
% Definir la función de transferencia G1(s)
num = [24 0]; % Numerador: 24s
den = conv(conv([1 0], [1 1]), [1 3]) + 24; % Denominador: s(s+1)(s+3) + 24

% Trazar el LGR
figure;
rlocus(tf(num, den));
title('Lugar de las Raíces (LGR) de G1(s)');
xlabel('Parte Real');
ylabel('Parte Imaginaria');
grid on;

