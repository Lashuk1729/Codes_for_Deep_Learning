import pandas as pd


def perceptron_AND(test_inputs):
    weights = [1, 1]
    bias = -1
    outputs = []

    # Generate and check output
    for test_input in test_inputs:
        linear_combination = weights[0] * test_input[0] + weights[1] * test_input[1] + bias
        output = int(linear_combination >= 1)
        outputs.append(output)

    return outputs

def perceptron_OR(test_inputs):

    weights = [1, 1]
    bias = -1
    outputs = []

    # Generate and check output
    for test_input in test_inputs:
        linear_combination = weights[0] * test_input[0] + weights[1] * test_input[1] + bias
        output = int(linear_combination >= 0)
        outputs.append(output)

    return outputs

def perceptron_XOR(test_inputs, correct_outputs):

    outputs = []

    # Generate and check output
    output_AND = perceptron_AND(test_inputs)
    output_OR = perceptron_OR(test_inputs)
    output_NAND = [0 if i == 1 else 1 for i in output_AND]

    test_input_XOR = [(x,y) for x,y in zip(output_OR, output_NAND)]
    
    output_XOR = perceptron_AND(test_input_XOR)
    
    # Generate and check output
    for test_input, output1, output2, output3, output4, correct_output in zip(test_inputs, output_AND, output_OR, output_NAND, output_XOR, correct_outputs):
        is_correct_string = 'Yes' if output4 == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], output1, output2, output3, output4, is_correct_string])

    output_frame = pd.DataFrame(outputs, columns=[
                                'Input 1', '  Input 2', '  AND Operation', '  OR Operation', '  NAND Operation', '  Activation Output', '  Is Correct'])
    
    print('Output for XOR Operation:')
    print(output_frame.to_string(index=False))
    

# Inputs and outputs for XOR Operation
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Manually setting: weight1, weight2, and bias for AND Perceptron
correct_outputs = [False, True, True, False]


# Output from perceptron_OR
outputs = perceptron_XOR(test_inputs, correct_outputs)
