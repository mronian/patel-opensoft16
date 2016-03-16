from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4, inch, landscape, letter
from reportlab.platypus import SimpleDocTemplate, Table, PageBreak, TableStyle, Paragraph,Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER
import cv2
import numpy as np
#Input = [["temp.jpg",[("Page1_plot1","X-Axis","Y-Axis",[(("Caption2",np.array([180,100,100])),[(10,20.3),(30,40)]),(("Caption3",np.array([180,100,100])),[(10,20),(30,40)])]),("Page1_plot2","X-Axis","Y-Axis",[(("Caption2",np.array([180,100,100])),[(10,20),(30,40)]),(("Caption3",np.array([180,100,100])),[(10,20),(30,40)])])]],
#         ["temp.jpg",[("Page2_plot1","X-Axis","Y-Axis",[(("Caption2",np.array([180,100,100])),[(10,20),(30,40)]),(("Caption3",np.array([180,100,100])),[(10,20),(30,40)])]),("Page2_plot2","X-Axis","Y-Axis",[(("Caption2",np.array([180,100,100])),[(10,20),(30,40)]),(("Caption3",np.array([180,100,100])),[(10,20),(30,40)])])]]]




def Output(Input):
    doc = SimpleDocTemplate("test.pdf", pagesize=letter, rightMargin=30,leftMargin=30, topMargin=30,bottomMargin=18)
    elements = []
    s = getSampleStyleSheet()
    s = s["BodyText"]
    s.wordWrap = 'CJK'
    s.fontsize = 8
    s.alignment = TA_CENTER
    for pages in Input:
             I = Image(pages[0])
             w,h = letter
             I.drawHeight = w*0.8*I.drawHeight/I.drawWidth
             I.drawWidth = w*0.8
             elements.append(I)
             elements.append(PageBreak())
             plots = pages[1]
             for plot in plots:
                 Plot_Caption = plot[0]
                 x_caption = plot[1]
                 y_caption = plot[2]
                 lines = plot[3]
                 data = [[Plot_Caption]]
                 style = TableStyle([('BOX', (0,0), (-1,-1), 0.25, colors.black),('ALIGN',(0,-1),(-1,-1),'CENTER')])
                 s.textColor = 'black'
                 data2 = [[Paragraph(cell, s) for cell in row] for row in data]
                 t=Table(data2) 
                 t.setStyle(style)
                 elements.append(t)
                 data = [[x_caption,y_caption,"Line"]]
                 style = TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('BOX', (0,0), (-1,-1), 0.25, colors.black)])
                 s.textColor = 'black'
                 data2 = [[Paragraph(cell, s) for cell in row] for row in data]
                 t=Table(data2) 
                 t.setStyle(style)
                 elements.append(t)
                 elements.append(Spacer(width=0, height=0.1*cm))
                 for line in lines:
                     line_caption = line[0][0]
                     line_color = line[0][1]
                     points = line[1]
                     data = []
                     for point in points:
                        data.append([str(point[0]) ,str(point[1]),line_caption])
                     style = TableStyle([('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),('BOX', (0,0), (-1,-1), 0.25, colors.black),('TEXTCOLOR',(0,0),(-1,-1),colors.blue)])
                     line_color = cv2.cvtColor(line_color,cv2.COLOR_HSV2BGR)
                     r = line_color[2]
                     g = line_color[1]
                     b = line_color[0]
                     col = '#'
                     col += '%02x' %r
                     col += '%02x' %g
                     col += '%02x' %b
                     s.textColor = col
                     data2 = [[Paragraph(cell, s) for cell in row] for row in data]
                     t=Table(data2) 
                     t.setStyle(style)
                     elements.append(t)
                     elements.append(Spacer(width=0, height=0.1*cm))
                 elements.append(Spacer(width=0, height=0.8*cm))
             elements.append(PageBreak())
    doc.build(elements)



