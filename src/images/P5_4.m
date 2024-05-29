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
