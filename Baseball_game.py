class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []

        for i in range(len(operations)):
            if  operations[i] == '+':
                record.append(record[-1] + record[-2])
            elif operations[i] == 'C':
                record.pop()
            elif operations[i] == 'D':
                double = record[-1] * 2
                record.append(double)
            else:
                z = int(operations[i])

                record.append(z)
        print(record)

        total = sum(record)
        return(total)
