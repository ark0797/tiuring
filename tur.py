class machine():
    def __init__(self):
        self.mech = {}
        mechload = open("mechanics5","r")
        reading = mechload.readline().replace("\n","")
        while reading:
            q0,first,q1,second,turn = reading.split()
            if q0 not in self.mech:
                self.mech[q0] = {"first":[first],"q1":[q1],"second":[second],"turn":[turn]}
            else:
                self.mech[q0]["first"].append(first)
                self.mech[q0]["q1"].append(q1)
                self.mech[q0]["second"].append(second)
                self.mech[q0]["turn"].append(turn)
            reading = mechload.readline().replace("\n","")
        inputfile = open("input5","r")
        self.inputtext = inputfile.readline()
        self.newtext = self.start("q0",2,self.inputtext)
        print(self.newtext)
    def start(self,q0,position,text):
        first = text[position]
        if q0 == "q13":
            return text
        for i in range(len(self.mech[q0]["first"])):
            if str(self.mech[q0]["first"][i]) == first:
                text = text[:position] + self.mech[q0]["second"][i] + text[position+1:]
                if self.mech[q0]["turn"][i] == "R":
                    newposition = position + 1
                else:
                    newposition = position - 1
                text = self.start(self.mech[q0]["q1"][i],newposition,text)
                break
        return text
do = machine()
