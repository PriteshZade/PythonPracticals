def slice(objects, parameters):
    if not isinstance(objects, (list, tuple, str)):
        return "TypeError: objects must be a list, tuple, or string"
    
    if isinstance(objects, tuple):
        objects = list(objects)
    elif isinstance(objects, str):
        objects = list(objects)
    
    start, end, step = 0, len(objects), 1

    if len(parameters) >= 1:
        start = parameters[0]
        if start < 0:
            start += len(objects)
        start = max(start, 0)

    if len(parameters) >= 2:
        end = parameters[1]
        if end < 0:
            end += len(objects)
        end = min(end, len(objects))

    if len(parameters) == 3:
        step = parameters[2]
        if step == 0:
            return "step cannot be zero"

    if len(parameters) > 3:
        return "Invalid parameters"

    result = []
    if step > 0:
        i = start
        while i < end:
            result.append(objects[i])
            i += step
    else:
        i = start
        while i > end:
            result.append(objects[i])
            i += step

    if isinstance(objects, tuple):
        return tuple(result)
    elif isinstance(objects, str):
        return ''.join(result)
    else:
        return result

print(slice([1, 2, 3, 4, 5], [1, 4]))  

