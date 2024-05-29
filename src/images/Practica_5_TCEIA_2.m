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

margin(num,den)

% Buscar las posiciones donde ks es igual a 0.3
posiciones = find(abs(ks - 0.3) < eps); % Usamos eps para manejar errores de precisión

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

%calcular duración del régimen transitorio del sistema
frecuencia = polos(1);
Ts1 = -4/(zetas(1)*frecuencia);
disp('Duración del régimen transitorio del sistema:');
disp(Ts1);

% Calcular la respuesta al escalón unitario del sistema
step_info = stepinfo(G_nueva);

% Obtener el tiempo de establecimiento (settling time)
Ts = step_info.SettlingTime;

% Calcular el error en estado estable para una entrada de tipo rampa con pendiente de 0.1 unidades
rampa_slope = 0.1;
ess_rampa = 0.1 / rampa_slope; % El error en estado estable para una rampa es 1/slope

% Mostrar el resultado
disp(['Error en estado estable para una entrada de tipo rampa con pendiente de 0.1 unidades: ', num2str(ess_rampa)]);
