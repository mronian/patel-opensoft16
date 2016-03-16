from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, inch, landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
Input = [
        [
            ("Page1_plot1","X-Axis","Y-Axis",
                [("Caption2",[(10,20),(30,40)]),
                    ("Caption3",[(10,20),(30,40)])]),
            ("Page1_plot2","X-Axis","Y-Axis",
                [("Caption2",[(10,20),(30,40)]),("Caption3",[(10,20),(30,40)])])],
        
        [("Page2_plot1","X-Axis","Y-Axis",[("Caption2",[(10,20),(30,40)]),("Caption3",[(10,20),(30,40)])]),("Page2_plot2","X-Axis","Y-Axis",[("Caption2",[(10,20),(30,40)]),("Caption3",[(10,20),(30,40)])])]]

def getOutput(Input):
    doc = SimpleDocTemplate("output.pdf", pagesize=letter, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    elements = []
    for page in Input:
             # elements.append(Image("img/page2.png"))
             for plot in page:
                 Plot_Caption = plot[0]
                 x_caption = plot[1]
                 y_caption = plot[2]
                 lines = plot[3]
                 data = [[Plot_Caption],[x_caption,y_caption,"Line"]]
                 for line in lines:
                     line_caption = line[0]
                     # import pdb; pdb.set_trace()
                     points = line[1]
                     for point in points:
                        data.append([str(point[0]) ,str(point[1]),line_caption])
                 style = TableStyle([('ALIGN',(1,1),(-2,-2),'RIGHT'),('TEXTCOLOR',(1,1),(-2,-2),colors.red),('VALIGN',(0,0),(0,-1),'TOP'),('TEXTCOLOR',(0,0),(0,-1),colors.blue),('ALIGN',(0,-1),(-1,-1),'CENTER'),('VALIGN',(0,-1),(-1,-1),'MIDDLE'),('TEXTCOLOR',(0,-1),(-1,-1),colors.green),('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),('BOX', (0,0), (-1,-1), 0.25, colors.black),])
                 s = getSampleStyleSheet()
                 s = s["BodyText"]
                 s.wordWrap = 'CJK'
                 data2 = [[Paragraph(cell, s) for cell in row] for row in data]
                 t=Table(data2)
                 t.setStyle(style)
                 elements.append(t)
    doc.build(elements)
