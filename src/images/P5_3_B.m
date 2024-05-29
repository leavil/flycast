clc; clear all;

% Definir la función de transferencia
num = 1;
den = [1 4 3 0]; % Denominador del sistema
G = tf(num, den);

% Encontrar el valor de K para el cual la respuesta es críticamente amortiguada
syms s K
polinomio_caracteristico = s^3 + 4*s^2 + 3*s + K;
soluciones = solve(diff(polinomio_caracteristico, s, 2) == 0, K);

% Obtener el valor real de K
K_critico = double(soluciones);
K_critico = K_critico(K_critico > 0);

% Mostrar el valor crítico de K
disp('Valor crítico de K para el cual el sistema es críticamente amortiguado:');
disp(K_critico);

% Comprobar mediante simulación
if ~isempty(K_critico)
    % Crear la función de transferencia en lazo cerrado con K_critico
    G_cl = feedback(K_critico * G, 1);

    % Mostrar los polos de la función de transferencia en lazo cerrado
    polos_cl = pole(G_cl);
    disp('Polos del sistema en lazo cerrado:');
    disp(polos_cl);

    % Verificar si los polos son reales e iguales
    es_criticamente_amortiguado = all(imag(polos_cl) == 0) && (length(unique(polos_cl)) < length(polos_cl));
    disp('¿El sistema es críticamente amortiguado?');
    disp(es_criticamente_amortiguado);

    % Simular la respuesta al escalón unitario del sistema en lazo cerrado
    figure;
    step(G_cl);
    title('Respuesta al escalón unitario del sistema críticamente amortiguado');
    grid on;
else
    disp('No se encontró un valor crítico de K para el cual el sistema sea críticamente amortiguado.');
end
