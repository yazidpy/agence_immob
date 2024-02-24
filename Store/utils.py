import pandas 

def array_to_dataframe(input_array, feature_names):
    if len(input_array) != len(feature_names):
        raise ValueError("Input array length doesn't match the number of feature names")

    data = [input_array]
    df = pandas .DataFrame(data, columns=feature_names)
    return df