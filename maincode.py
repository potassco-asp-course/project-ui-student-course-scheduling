from IPython.core.magic import register_line_magic
import clingo
from clingo.control import Control

from IPython.display import display
import ipywidgets as widgets

class main:
    def __init__(self):
        self.sem = 0

        self.course = widgets.Textarea(
            description='Enter course:',
            placeholder='Ex. asp',
            ensure_option=True,
            disabled=False
        )
        self.btn_save_course = widgets.Button(
            description='Save course',
            disabled=False,
            button_style='success'
        )
        self.semester = widgets.BoundedIntText(
            description='Semester:', 
            min=2, 
            max=6
        )

        self.btn_save_semester = widgets.Button(
            description='Save semester',
            disabled=False,
            button_style='success'
        )

        self.output = widgets.Output()


        def update(fact):
            result = fact+";"#+result
            with output:
                display(result)

        ui_top = widgets.VBox([widgets.Label(value='Course',style=dict(font_weight='bold')), self.course, self.btn_save_course, self.output])

        ui_btm = widgets.VBox([widgets.Label(value='Semester',style=dict(font_weight='bold')), self.semester, self.btn_save_semester])

        self.ui = widgets.VBox([ui_top,ui_btm])

        def save_course(bttn):
            output_file = open('user_course.lp', 'a') 
            output_file.write('course('+self.course.value+').') 
            output_file.close() 

        def save_semester(bttn):
            self.sem = self.semester.value

        self.btn_save_course.on_click(save_course)
        self.btn_save_semester.on_click(save_semester)