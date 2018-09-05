function case_test()
    % test ways of having multiple methods in codes, and compare speeds

    % preallocate
    etc = zeros(1, 5); % elapsed time for switch-case
    eti = zeros(1, 5); % elapsed time for if-then

    % do five, sequential depths of tests
    for i = 1:5
        
        % x is the method 'name'
        x = ['test', num2str(i)];

        % switch-case test
        disp(['with cases, x = ', num2str(i)])
        tic
        for j = 1:1e6
            [y] = with_case(x);
        end
        etc(i) = toc;
       
        % if-then test
        disp(['with ifs, x = ', num2str(i)])
        tic
        for j = 1:1e6
            [y] = with_ifs(x);
        end
        eti(i) = toc;
        
    end

    % no methods test for comparison
    disp('without cases')
    tic
    for j = 1:1e6
        [y] = without_case(x);
    end
    et0 = toc;
    
    
    % plot the results
    figure(); hold on;
    plot(1:5, etc, 'o-', 'LineWidth', 1.2)
    plot(1:5, eti, 'o-', 'LineWidth', 1.2)
    plot([1, 5], [et0, et0], 'k-')
    text(0.6, 0.05, 'no cases', 'Units', 'Normalized')
    xlabel('number of cases (depth)')
    ylabel('elapsed time for 1e6 runs (s)')
    legend('switch-case', 'if-then', 'no methods', 'Location', 'NorthWest')
    box on
    
end


function [y] = with_case(x)
    switch x
        case 'test1'
            y = 1;
        case 'test2'
            y = 2;
        case 'test3'
            y = 3;
        case 'test4'
            y = 4;
        case 'test5'
            y = 5;
    end
end


function [y] = with_ifs(x)
    if strcmp(x, 'test1')
        y = 1;
    elseif strcmp(x, 'test2')
        y = 2;
    elseif strcmp(x, 'test3')
        y = 3;
    elseif strcmp(x, 'test4')
        y = 4;
    elseif strcmp(x, 'test5')
        y = 5;
    end
end


function [y] = without_case(x)
    y = 5;
end
