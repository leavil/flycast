clc; clear all;

% Definir la función de transferencia
num = 1;
den = [1 4 3 0]; % Denominador del sistema
G = tf(num, den);

% Trazar el lugar de raíces
figure;
rlocus(G)
sgrid

% Especificar la línea de zeta = 1 en el gráfico del lugar de raíces
zeta = 1;
sgrid(zeta, [])

% Buscar el valor de K para zeta = 1
[k, poles] = rlocfind(G);

% Mostrar el valor de K encontrado y los polos correspondientes
disp(['El valor de K para una respuesta críticamente amortiguada es: ', num2str(k)]);
disp('Los polos correspondientes son:');
disp(poles);

% Crear la función de transferencia de lazo cerrado con el valor de K encontrado
G_cl = feedback(k * G, 1);

% Verificar la respuesta al escalón unitario
figure;
step(G_cl)
title('Respuesta al Escalón del Sistema Críticamente Amortiguado');
grid on;

% Obtener información de la respuesta al escalón
step_info = stepinfo(G_cl);

% Mostrar la información de la respuesta al escalón
disp('Información de la respuesta al escalón:');
disp(step_info);
