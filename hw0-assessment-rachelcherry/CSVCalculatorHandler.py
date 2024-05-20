import Calculator 
import csv

class CSVCalculatorHandler:
    def __init__(self, calc):
        self.calculator = Calculator.Calculator()
        # self.addition = self.calculator.add(2,3)
        # print(self.addition)
        # print(self.calculator)
        self.history = [[]]

    def process_csvs(self, filenames, output_prefix="output"):
        solution = [[]]
        string_op = ""
        answer = None
        count = 0
        for file in filenames:
                with open(file, 'r') as csv_file: # open the csv input file for reading
                    lines = csv.reader(csv_file) #read the lines in the file 
                    for line in lines:
                        try:
                            operation_done = line[-1]
                            operands = line[:-1]
                            float_operands = []
                            for i in operands:
                                float_operands.append(float(i))
                            if operation_done == "multiply":
                                if len(line) < 2:
                                        answer = None
                                        error = 2
                                else:
                                    print(float_operands)
                                    answer = self.calculator.multiply(float_operands)
                                    operation = "multiply"
                            elif operation_done == "add":
                                if len(line) < 2:
                                    answer = None
                                    error = 2
                                else:
                                    answer = self.calculator.add(float_operands)
                                    error = 0
                                    operation = "add"

                            elif operation_done == "divide":
                                if len(float_operands) != 2:
                                    answer = None
                                    error = 2
                                else:
                                    if float_operands[1] != 0:
                                        answer = self.calculator.division(float_operands)
                                        error = 0
                                        operation = "divide"
                                    else:
                                        answer = None
                                        error = 1
                            elif operation_done == "exponentiate":
                                if len(float_operands) != 2:
                                    error = 2
                                    answer = None
                                else:
                                    answer = self.calculator.exp(float_operands)
                                    error = 0
                                    operation = "exponentiate"
                            elif operation_done == "subtract":
                                if len(line) < 2:
                                    error = 2
                                    answer = None
                                else:
                                    answer = self.calculator.subtract(float_operands)
                                    error = 0
                                    operation = "subtract"
                            else:
                                answer = None
                                error = 3
                        except:
                            error = 4
                            answer = None
                        i = 0
                        while i != len(operands):
                            string_op += operands[i] + ","
                            i+=1
                        string_op += operation_done
                        solution.append([answer, error])
                        self.save_to_history(file, string_op, answer, error)
                        # save history
                        file_name = f'{output_prefix}_{count}.csv'
                        
                        with open(file_name, 'w') as file_2:
                            file_output = csv.writer(file_2)
                            for i in solution:
                                file_output.writerow(i)
        count += 1                

            


    def save_to_history(self, filename, operation, result, error_code):
        self.history.append([filename, operation, result, error_code])
        

    def history_export(self, export_filename):   
        with open(export_filename, 'w') as exported:
            export = csv.writer(exported)
            i = 0
            while i != len(self.history):
                export.writerow(self.history[i])
                i+=1



if __name__ == '__main__':
    x = ['input.csv']
    instance = CSVCalculatorHandler(Calculator)
    instance.process_csvs(x)
    instance.history_export("history.txt")
   
