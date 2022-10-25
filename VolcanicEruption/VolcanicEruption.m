clc
clear
clf

% Variables
v0=138.9;
y0=5426;
ang=60;
d=0.4;
g=9.8;
c= 0.25 * d^2;
v0x=v0.*cosd(ang);
v0y=v0.*sind(ang);
m=55;

disp('Las variables por default son:')
disp('Velocidad inicial = 138.9m/s')
disp('Altura inicial = 5426m')
disp('Angulo de disparo = 60º')
disp('Diametro de la roca = 0.4m,')
ingresa_variables=input('Deseas usar los valores por defualt (ingresa 1) o prefieres ingresar nuevos valores (ingresa 2)? (D/N): ');

if ingresa_variables == 2
    v0=input('Cual es la velocidad inicial (m/s): ');
    y0=input('Cual es la altura inicial (metros): ');
    ang=input('Cual es el angulo de disparo: ');
    d=input('Cual es el diámetro de la roca piroclástica? (metros): ');
end

n = 5;
diam = 250;
base = n * diam;
figure(1);
clf;
x = [0 (base/2) - (diam/2) (base/2) + (diam/2) base];
y = [0 y0 y0 0];
patch(x,y,'Red')

d1 = (base/2) - (diam/2);
d2 = (base/2) + (diam/2);

x0 = randi([d1 d2]);

%Vectores
t0=0;
tf=90;
dt=0.01;
t=t0:dt:tf;
np=length(t);
y=zeros(1,np);
x=zeros(1,np);
vy=zeros(1,np);
vx=zeros(1,np);

%Valores iniciales
y(1)=y0;
vx(1)=v0x;
x(1)=x0;
vy(1)=v0y;


%Euler
for j=1:np-1
    vx(j+1)=vx(j)+(dt*((-c/m)*vx(j)*sqrt((vx(j)^2)+(vy(j)^2))));
    x(j+1)=x(j)+dt*vx(j);
    
    vy(j+1)=vy(j)+(dt*((-c/m)*vy(j)*sqrt((vx(j)^2)+(vy(j)^2))-g));
    y(j+1)=y(j)+dt*vy(j);

    if y(j+1) < 0
        y(j+1) = 0;
    end
end

figure(1)
hold on

comet(x,y)


for j=1:np-1
    vx(j+1)=vx(j);
    x(j+1)=x(j)+dt*vx(j);

    vy(j+1)=vy(j)-dt*g;
    y(j+1)=y(j)+dt*vy(j);

    if y(j+1) < 0
        y(j+1) = 0;
        x(j+1) = x(j);
        
    end

    

end
    
figure(1)
hold on
comet(x,y)






