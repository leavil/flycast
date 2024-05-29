Gp=tf([1],[0.25 1 0])
Ts=0.05;
figure(1)
rlocus(Gp)
sgrid

[nd,dd]=c2dm(1,[0.25 1 0],Ts,'zoh');
nd
dd

figure(2)
zgrid
hold
rlocus(nd,dd)
