def function_01(param1):
    def actual(param2):
        return param1 ** param2
    return actual

square = function_01(3)(2);
cube = function_01(2)(3);

print(square);
print(cube);                                       