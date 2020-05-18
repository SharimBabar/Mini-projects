import xlsxwriter
class trainer:
    def __init__(self, name, module, batch):
        self.name=name
        self.module=module
        self.batch=batch
    def trainer_name(self):
        return trainer.name
    def trainer_module(self):
        return  trainer.module
    def trainer_batch(self):
        return trainer.batch

trainer_1=trainer('Guy1', 'Data stream',1)
trainer_2=trainer('Guy2', 'Java stream', 2)


class batch (trainer):
    def __init__(self, student_ID, name, module, start_date,  batch_no):
        self.student_ID=student_ID
        self.name=name
        self.module=module
        self.start_date=start_date
        self.batch_no=batch_no

    def studnet_name(self):
        return batch.name
    def studentID(self):
        return batch.student_ID
    def student_module(self):
        return batch.module
    def student_batch(self):
        return batch.batch_no




student_1=batch(101,'Davy1', 'Data Stream','30/09/2019',1)
student_2=batch(696,'Davy2', 'Data Stream', '30/09/2019',1)
student_3=batch(420,'Davy3', 'Data stream','30/09/2019',1)
student_4=batch(611, 'Davy4', 'Data stream','30/09/2019',1)
student_5=batch(323, 'Davy5', 'Data Stream','30/09/2019',1)
student_6=batch(455,'Davy6','Data stream','30/09/2019',1)
student_7=batch(288,'Davy7', 'Data stream', '30/09/2019',1)

print(trainer_1.batch)
print(student_1.batch_no)
def listing(batch):
    list=[]
    list.append(batch.student_ID)
    list.append(batch.name)
    list.append(batch.module)
    list.append(batch.start_date)
    list.append(batch.batch_no)
    return list

def list_trainer(trainer):
    list_trainer =[]
    list_trainer.append(trainer.name)
    list_trainer.append(trainer.module)
    list_trainer.append(trainer.batch)
    return list_trainer

workbook=xlsxwriter.Workbook('Batch.xlsx')

worksheet_Student=workbook.add_worksheet()

worksheet_Student.write('A1','Student ID')
worksheet_Student.write('B1','Name',)
worksheet_Student.write('C1', 'Module')
worksheet_Student.write('D1', 'Start Date')
worksheet_Student.write('E1','Batch no')

def xl(list, workbook, n_rol):
    x=int(n_rol)
    for item in range(len(list)):
      workbook.write(1+x,item,list[item])

xl(listing(student_1),worksheet_Student,0)
xl(listing(student_2),worksheet_Student,1)
xl(listing(student_3),worksheet_Student,2)
xl(listing(student_4),worksheet_Student,3)
xl(listing(student_5), worksheet_Student,4)
xl(listing(student_6),worksheet_Student,5)
xl(listing(student_7), worksheet_Student,6)

worksheet_trainer=workbook.add_worksheet()

worksheet_trainer.write('A1', 'Name')
worksheet_trainer.write('B1','Module')
worksheet_trainer.write('C1', 'Batch')

xl(list_trainer(trainer_1),worksheet_trainer, 0)
xl(list_trainer(trainer_2),worksheet_trainer, 1)
workbook.close()

