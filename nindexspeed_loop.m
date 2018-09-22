
BV = zeros(10000, 10000);
ne = numel(BV);
rv = randi(ne, 50, 1);

t = NaN(size(rv));

for i = 1:size(rv, 1)
    i
    idx = rv(1:i);
    
    tic
    for j = 1:1e6
        a = BV(idx);
    end    
    t(i) = toc;

end

figure()
plot(1:size(rv, 1), t, 'o-')
xlabel('number of elements indexed')
ylabel('time for 1e6 loops (s)')


