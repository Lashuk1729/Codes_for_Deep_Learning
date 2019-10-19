import pandas as pd


def perceptron_AND(test_input, weights, bais, correct_outputs):

    outputs = []
    # Generate and check output
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = weights[0] * test_input[0] + weights[1] * test_input[1] + bias
        output = int(linear_combination >= 0)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

    # Print output
    num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
    print('Output for AND Operation:')
    if not num_wrong:
        print('Nice!  We got it all correct.\n')
    else:
        print('We got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))
    print('\n\n')

    return output


def perceptron_OR(test_input, weights, bais, correct_outputs):

    outputs = []
    # Generate and check output
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = weights[0] * test_input[0] + weights[1] * test_input[1] + bias
        output = int(linear_combination >= 0)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

    # Print output
    num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
    print('Output for OR Operation:')
    if not num_wrong:
        print('Nice!  We got it all correct.\n')
    else:
        print('We got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))
    print('\n\n')

    return output


def perceptron_NOT(test_input, weights, bais, correct_outputs):

    outputs = []
    # Generate and check output
    for test_input, correct_output in zip(test_inputs, correct_outputs):
        linear_combination = weights * test_input + bias
        output = int(linear_combination >= 0)
        is_correct_string = 'Yes' if output == correct_output else 'No'
        outputs.append([test_input, linear_combination, output, is_correct_string])

    # Print output
    num_wrong = len([output[4] for output in outputs if output[3] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=[
                                'Input', '  Linear Combination', '  Activation Output', '  Is Correct'])
    print('Output for NOT Operation:')
    if not num_wrong:
        print('Nice!  We got it all correct.\n')
    else:
        print('We got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))

    return output

# Inputs and outputs for AND/OR Operation
test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Manually setting: weight1, weight2, and bias for AND Perceptron
correct_outputs = [False, False, False, True]
weights = [0.5, 0.5]
bias = -1

# Output from perceptron_AND
outputs = perceptron_AND(test_inputs, weights, bias, correct_outputs)


# Manually setting: weight1, weight2, and bias for OR Perceptron
correct_outputs = [False, True, True, True]
weights = [0.5, 0.5]
bias = -0.5

# Output from perceptron_OR
outputs = perceptron_OR(test_inputs, weights, bias, correct_outputs)

# Inputs and outputs for AND/OR Operation
test_inputs = [0, 1]

# Manually setting: weight1, weight2, and bias for AND Perceptron
correct_outputs = [True, False]
weights = -2
bias = 1

# Output from perceptron_NOT
outputs = perceptron_NOT(test_inputs, weights, bias, correct_outputs)
