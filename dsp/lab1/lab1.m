% Задаем исходные параметры сигнала
% Для Гаусса
A = 1;
sigma = 5;
% Для rect
c = 5;

% Вводим параметры дискретизации
n = input('Input number of samples: ');
dt = input('Input sample step: ');
t_max = dt * (n - 1) / 2;

% Исходный сигнал
x = -t_max:0.005:t_max;

gauss_reference = A * exp(-(x/sigma).^2);

rect_reference = zeros(size(x));
rect_reference(abs(x) - c < 0) = 1;


% Дискретизация 
t = -t_max:dt:t_max; 

gauss_discrete = A * exp(-(t / sigma).^2);

rect_discrete = zeros(size(t));
rect_discrete(abs(t) - c < 0) = 1;

% Восстанавиваем сигнал 
gauss_restored = zeros(1, length(x));
rect_restored = zeros(1, length(x));
for i=1:length(x)
   for j = 1:n
       gauss_restored(i) = gauss_restored(i) + gauss_discrete(j) *  sin(pi*(x(i)-t(j))/dt)/(pi*(x(i)-t(j))/dt);
       rect_restored(i) = rect_restored(i) + rect_discrete(j) * sin(pi*(x(i)-t(j))/dt)/(pi*(x(i)-t(j))/dt);
   end
end

figure;
subplot(2,1,1);
title('Rect');
hold on;
grid on;
plot(x, rect_reference, 'b');
plot(x, rect_restored, 'k');
plot(t, rect_discrete, '.m');
legend('Исходный', 'Восстановленный', 'Дискретный');

subplot(2,1,2);
title('Гаусс');
hold on;
grid on;
plot(x, gauss_reference, 'b');
plot(x, gauss_restored, 'k');
plot(t, gauss_discrete, '.m');
legend('Исходный', 'Восстановленный', 'Дискретный');

print -dpng plot1.png;