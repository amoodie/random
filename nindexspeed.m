
BV = zeros(10000, 10000);
ne = numel(BV);
rv = randi(ne, 26, 1);


ai = rv(1);
tic
for i = 1:1e6
    aidx = BV(ai);
end
a = toc;


bi = rv(1:2);
tic
for i = 1:1e6
    bidx = BV(bi);
end
b = toc;


ci = rv(1:3);
tic
for i = 1:1e6
    cidx = BV(ci);
end
c = toc;


di = rv(1:4);
tic
for i = 1:1e6
    didx = BV(di);
end
d = toc;


zi = rv(1:26);
tic
for i = 1:1e6
    zidx = BV(zi);
end
z = toc;



figure()
plot([1:4, 26], [a, b, c, d, z], 'o-')
xlabel('number of elements indexed')
ylabel('time for 1e6 loops (s)')


