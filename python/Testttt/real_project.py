import pickle
from tkinter import *
from tkinter import messagebox 
from datetime import datetime
from abc import ABC, abstractmethod
try:
    from tkcalendar import Calendar
except:
    warning = "In order to use the set deadline button, install tkcalendar by typing \"pip install tkcalendar\" in your terminal."
    print(warning)
    messagebox.showwarning("Warning", warning) 

class Date(object):
    def get_date_diff(self, deadline):
        #get today's date
        today = datetime.now().strftime("%d/%m/%Y")

        #convert string to date object
        d1 = datetime.strptime(today, "%d/%m/%Y")
        try:
            d2 = datetime.strptime(deadline, "%d/%m/%Y")
        except:
            return 999999
        
        difference = d2 - d1
        return difference.days
    

class StatsWindow(ABC, Toplevel):
    def __init__(self, parent, title, stats):
        super().__init__(parent)
        self.parent = parent
        self.title(title)
        self.geometry("550x200")
        self.minsize(550, 200)
        self.stats = stats
        
        #create margins
        self.margin_top = Frame(self, height=15)
        self.margin_1 = Frame(self, width=15)
        self.margin_2 = Frame(self, width=15)
        self.margin_3 = Frame(self, width=15)
        self.margin_bottom = Frame(self, height=15)
        self.margin_top.grid(row=1, column=1, columnspan=7)
        self.margin_1.grid(row=2, column=1, sticky=W)
        self.margin_2.grid(row=2, column=3)
        self.margin_3.grid(row=2, column=5, sticky=E)
        self.margin_bottom.grid(row=3, column=1, columnspan=7)
        
        #expand margins
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

    @abstractmethod
    def create_stats(self):
        pass


class GeneralStatsWindow(StatsWindow):
    def __init__(self, parent, title, stats):
        super().__init__(parent, title, stats)
        self.geometry("280x150")
        self.minsize(280, 150)

        self.create_stats()
        self.margin_3.grid_forget()

    def create_stats(self):
        gen_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15
        )
        gen_frame.grid(row=2, column=2, sticky=EW)
        #expand frame horizontally
        self.grid_columnconfigure(2, weight=1)

        gen_label = Label(gen_frame, text="General Statistics", width=30, font=("Helvetica", 9, "bold"))
        gen_label.grid(row=1, column=1, columnspan=2, pady=(0,10))

        active_label = Label(gen_frame, text="Active:")
        active_label.grid(row=2, column=1, sticky=W)
        active_value = Label(gen_frame, text=self.stats["active"])
        active_value.grid(row=2, column=2, sticky=E)
        completed_label = Label(gen_frame, text="Completed:")
        completed_label.grid(row=3, column=1, sticky=W)
        completed_value = Label(gen_frame, text=self.stats["completed"])
        completed_value.grid(row=3, column=2, sticky=E)
        total_label = Label(gen_frame, text="Total:")
        total_label.grid(row=4, column=1, sticky=W)
        total_value = Label(gen_frame, text=self.stats["total"])
        total_value.grid(row=4, column=2, sticky=E)

        #expand widgets in frame
        gen_frame.grid_columnconfigure(1, weight=1)
        gen_frame.grid_columnconfigure(2, weight=1)


class PriorityStatsWindow(StatsWindow):
    def __init__(self, parent, title, stats):
        super().__init__(parent, title, stats)
        self.create_stats()
        #expand frames horizontally
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(4, weight=1)

    def create_stats(self):
        active_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15
        )
        active_frame.grid(row=2, column=2, sticky=EW)

        prio_label = Label(active_frame, text="Current Priority Statistics", width=30, font=("Helvetica", 9, "bold"))
        prio_label.grid(row=1, column=1, columnspan=2, pady=(0,10))

        high_label = Label(active_frame, text="High:")
        high_label.grid(row=2, column=1, sticky=W)
        high_value = Label(active_frame, text=self.stats["prio_high"])
        high_value.grid(row=2, column=2, sticky=E)
        medium_label = Label(active_frame, text="Medium:")
        medium_label.grid(row=3, column=1, sticky=W)
        medium_value = Label(active_frame, text=self.stats["prio_medium"])
        medium_value.grid(row=3, column=2, sticky=E)
        low_label = Label(active_frame, text="Low:")
        low_label.grid(row=4, column=1, sticky=W)
        low_value = Label(active_frame, text=self.stats["prio_low"])
        low_value.grid(row=4, column=2, sticky=E)
        none_label = Label(active_frame, text="None:")
        none_label.grid(row=5, column=1, sticky=W)
        none_value = Label(active_frame, text=self.stats["prio_none"])
        none_value.grid(row=5, column=2, sticky=E)

        #expand widgets in frame
        active_frame.grid_columnconfigure(1, weight=1)
        active_frame.grid_columnconfigure(2, weight=1)
        
        total_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15
        )
        total_frame.grid(row=2, column=4, sticky=EW)

        prio_label = Label(total_frame, text="Total Priority Statistics", width=30, font=("Helvetica", 9, "bold"))
        prio_label.grid(row=1, column=1, columnspan=2, pady=(0,10))

        high_all_label = Label(total_frame, text="High:")
        high_all_label.grid(row=2, column=1, sticky=W)
        high_all_value = Label(total_frame, text=self.stats["prio_high_all"])
        high_all_value.grid(row=2, column=2, sticky=E)
        medium_all_label = Label(total_frame, text="Medium:")
        medium_all_label.grid(row=3, column=1, sticky=W)
        medium_all_value = Label(total_frame, text=self.stats["prio_medium_all"])
        medium_all_value.grid(row=3, column=2, sticky=E)
        low_all_label = Label(total_frame, text="Low:")
        low_all_label.grid(row=4, column=1, sticky=W)
        low_all_value = Label(total_frame, text=self.stats["prio_low_all"])
        low_all_value.grid(row=4, column=2, sticky=E)
        none_all_label = Label(total_frame, text="None:")
        none_all_label.grid(row=5, column=1, sticky=W)
        none_all_value = Label(total_frame, text=self.stats["prio_none_all"])
        none_all_value.grid(row=5, column=2, sticky=E)

        #expand widgets in frame
        total_frame.grid_columnconfigure(1, weight=1)
        total_frame.grid_columnconfigure(2, weight=1)


class TagsStatsWindow(StatsWindow):
    def __init__(self, parent, title, stats):
        super().__init__(parent, title, stats)
        self.create_stats()
        #expand frames horizontally
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(4, weight=1)

    def create_stats(self):
        active_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15
        )
        active_frame.grid(row=2, column=2, sticky=EW)

        tags_label = Label(active_frame, text="Current Tags Statistics", width=30, font=("Helvetica", 9, "bold"))
        tags_label.grid(row=1, column=1, columnspan=2, pady=(0,10))

        personal_label = Label(active_frame, text="Personal:")
        personal_label.grid(row=2, column=1, sticky=W)
        personal_value = Label(active_frame, text=self.stats["tag_personal"])
        personal_value.grid(row=2, column=2, sticky=E)
        family_label = Label(active_frame, text="Family:")
        family_label.grid(row=3, column=1, sticky=W)
        family_value = Label(active_frame, text=self.stats["tag_family"])
        family_value.grid(row=3, column=2, sticky=E)
        friend_label = Label(active_frame, text="Friend:")
        friend_label.grid(row=4, column=1, sticky=W)
        friend_value = Label(active_frame, text=self.stats["tag_friend"])
        friend_value.grid(row=4, column=2, sticky=E)
        work_label = Label(active_frame, text="Work:")
        work_label.grid(row=5, column=1, sticky=W)
        work_value = Label(active_frame, text=self.stats["tag_work"])
        work_value.grid(row=5, column=2, sticky=E)
        entertainment_label = Label(active_frame, text="Entertainment:")
        entertainment_label.grid(row=6, column=1, sticky=W)
        entertainment_value = Label(active_frame, text=self.stats["tag_entertainment"])
        entertainment_value.grid(row=6, column=2, sticky=E)

        #expand widgets in frame
        active_frame.grid_columnconfigure(1, weight=1)
        active_frame.grid_columnconfigure(2, weight=1)

        total_frame = Frame(
            self,
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15
        )
        total_frame.grid(row=2, column=4, sticky=EW)

        tags_all_label = Label(total_frame, text="Total Tags Statistics", width=30, font=("Helvetica", 9, "bold"))
        tags_all_label.grid(row=1, column=1, columnspan=2, pady=(0,10))

        personal_all_label = Label(total_frame, text="Personal:")
        personal_all_label.grid(row=2, column=1, sticky=W)
        personal_all_value = Label(total_frame, text=self.stats["tag_personal_all"])
        personal_all_value.grid(row=2, column=2, sticky=E)
        family_all_label = Label(total_frame, text="Family:")
        family_all_label.grid(row=3, column=1, sticky=W)
        family_all_value = Label(total_frame, text=self.stats["tag_family_all"])
        family_all_value.grid(row=3, column=2, sticky=E)
        friend_all_label = Label(total_frame, text="Friend:")
        friend_all_label.grid(row=4, column=1, sticky=W)
        friend_all_value = Label(total_frame, text=self.stats["tag_friend_all"])
        friend_all_value.grid(row=4, column=2, sticky=E)
        work_all_label = Label(total_frame, text="Work:")
        work_all_label.grid(row=5, column=1, sticky=W)
        work_all_value = Label(total_frame, text=self.stats["tag_work_all"])
        work_all_value.grid(row=5, column=2, sticky=E)
        entertainment_all_label = Label(total_frame, text="Entertainment:")
        entertainment_all_label.grid(row=6, column=1, sticky=W)
        entertainment_all_value = Label(total_frame, text=self.stats["tag_entertainment_all"])
        entertainment_all_value.grid(row=6, column=2, sticky=E)

        #expand widgets in frame
        total_frame.grid_columnconfigure(1, weight=1)
        total_frame.grid_columnconfigure(2, weight=1)


class TaskCreator(Frame, Date):
    def __init__(self, parent, callback):
        super().__init__(parent)
        self.parent = parent
        self.callback = callback

        #frame decoration
        self.config(
            highlightbackground="black", 
            highlightthickness=2, 
            padx=15, 
            pady=15
        )

        #task input section
        task_label = Label(self, text="Insert Task")
        task_label.grid(row=1, column=1, sticky=NW, padx=(0, 5))
        self.task_input = Text(self, width=40, height=3)
        self.task_input.grid(row=1, column=2, columnspan=20)

        #deadline section
        self.deadline = StringVar(value="")
        deadline_label = Label(self, text="Deadline")
        deadline_button = Button(self, text="Set Deadline", command=self.open_calendar)
        deadline_display = Label(self, textvariable=self.deadline, width=8, anchor=W)
        deadline_remove = Button(self, text="Remove", command=lambda: self.deadline.set(""))
        deadline_label.grid(row=2, column=1, sticky=W, padx=(0,5), pady=10)
        deadline_button.grid(row=2, column=2, sticky=W, pady=10)
        deadline_display.grid(row=2, column=3, sticky=W, padx=5)
        deadline_remove.grid(row=2, column=5, sticky=W, padx=5)

        #priority section(default is None)
        priority_label = Label(self, text="Priority")
        priority_label.grid(row=3, column=1, sticky=W)
        text_to_value = {
            "None": "gray",
            "Low": "blue",
            "Medium": "yellow",
            "High": "red"
        }
        self.radio_var_priority = StringVar(value="gray")
        for i, (text, value) in enumerate(text_to_value.items()):
            radio = Radiobutton(
                self, 
                text=text, 
                variable=self.radio_var_priority, 
                value=value
            )
            radio.grid(row=3, column=i+2, sticky=W)

        #color section(default is black)
        text_color_label = Label(self, text="Text Color")
        text_color_label.grid(row=4, column=1, sticky=W)
        color_to_value = {
            "Black": "black",
            "Blue": "blue",
            "Red": "red"
        }
        self.radio_var_color = StringVar(value="black")
        for i, (color, value) in enumerate(color_to_value.items()):
            radio = Radiobutton(
                self, 
                text=color, 
                variable=self.radio_var_color, 
                value=value
            )
            radio.grid(row=4, column=i+2, sticky=W)

        #tags section
        tags_label = Label(self, text="Tags")
        tags_label.grid(row=5, column=1, sticky=W)
        self.checkboxes = {}
        tags = ["Personal", "Family", "Friend", "Work", "Entertainment"]
        for i, tag in enumerate(tags):
            self.on_off = IntVar()
            checkbox = Checkbutton(self, text=tag, variable=self.on_off, onvalue=1, offvalue=0)
            if i < 3:
                checkbox.grid(row=5, column=i+2, sticky=W)
            elif tag == "Entertainment":
                checkbox.grid(row=6, column=i-1, columnspan=2, sticky=W)
            else:
                checkbox.grid(row=6, column=i-1, sticky=W)
            self.checkboxes[tag] = self.on_off

        #task button section
        create_task_button = Button(
            self, text="Create Task", anchor=CENTER, command=self.create_activity
        )
        create_task_button.grid(row=7, column=3, pady=(10, 0))

    def create_activity(self):
        task = self.get_task_input()
        prio = self.get_priority_input()
        color = self.get_color_input()
        tags = self.get_tags_input()
        deadline = self.get_deadline()

        self.callback(task, prio, color, tags, deadline)
        self.reset_form()

    def open_calendar(self):
        calendar = CalendarWindow(self)
        self.parent.wait_window(calendar)  #wait for calendar to close
        selected_date = calendar.get_deadline()
        if selected_date:
            self.deadline.set(selected_date)
    

    def get_task_input(self):
        return self.task_input.get("1.0", "end-1c")

    def get_priority_input(self):
        return self.radio_var_priority.get()

    def get_color_input(self):
        return self.radio_var_color.get()
    
    def get_tags_input(self):
        checkboxes_true_values = {}
        for tag in self.checkboxes:
            checkboxes_true_values[tag] = self.checkboxes[tag].get()

        return checkboxes_true_values
    
    def get_deadline(self):
        return self.deadline.get()
    
    def reset_form(self):
        self.task_input.delete("1.0", END)
        self.radio_var_priority.set(value="gray")
        self.radio_var_color.set(value="black")
        for tag in self.checkboxes:
            self.checkboxes[tag].set(0)
        self.deadline.set("")


class TaskDisplay(Frame, Date):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        #frame decoration
        self.config(
            highlightbackground="black",
            highlightthickness=2,
            padx=15,
            pady=15
        )

        self.activityLabel = Label(self, text="Activities")
        self.activityLabel.pack()

        self.canvas = Canvas(self, width=350, height=500)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        scrollbar = Scrollbar(self, orient=VERTICAL, command=self.canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        self.task_list_frame_inner = Frame(self.canvas)
        self.task_list_frame_inner.pack(fill=BOTH, expand=True)
        self.canvas.create_window((0, 0), window=self.task_list_frame_inner, anchor=NW)

        self.activities = []
        self.completed = []

    def on_mousewheel(self, event):
        x, y = event.x_root, event.y_root
        if (self.canvas.winfo_rootx() <= x <= (self.canvas.winfo_rootx() + self.canvas.winfo_width()) and 
            self.canvas.winfo_rooty() <= y <= (self.canvas.winfo_rooty() + self.canvas.winfo_height()) and 
            len(self.activities) > 0
        ):
            self.canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def add_activity(self, task, prio, color, tags, deadline):
        #add container frame
        new_frame = Frame(
            self.task_list_frame_inner,
            highlightbackground=prio,
            highlightthickness=2,
        )
        new_frame.grid(column=1)

        #add task
        task_label = Label(
            new_frame,
            text=task,
            width=46,
            wraplength=290,
            justify=LEFT,
            anchor=W,
            fg=color,
            highlightbackground="black",
            highlightthickness=1
        )
        task_label.grid(row=1, column=1, columnspan=5, padx=5, pady=5, sticky=W)

        #add deadline
        if deadline != "":
            deadline_label = Label(new_frame, text=deadline, fg="red")
            deadline_label.grid(row=2, column=1, padx=5, sticky=W)

        #add tags
        if any(value == 1 for value in tags.values()):
            all_tags = ""
            for tag in tags:
                if tags[tag] == 1:
                    all_tags += f"#{tag}  "
            tag_label = Label(new_frame, text=all_tags, fg="orange")
            tag_label.grid(row=3, column=1, padx=5, sticky=W)

        #add complete button
        complete_button = Button(
            new_frame,
            text="Complete",
            command=lambda frame=new_frame: self.remove_activity(frame),
        )
        complete_button.grid(row=4, column=1, columnspan=5, pady=5)

        #store each frame's data
        sorting_key = (self.get_date_diff(deadline), self.get_priority_value(prio))
        new_frame.sorting_key = sorting_key
        new_frame.task_label = task_label
        new_frame.deadline_label = deadline_label if deadline != "" else None
        new_frame.prio = prio
        new_frame.tags = tags
        self.activities.append(new_frame)

        #sort and update activities
        self.activities.sort(key=lambda frame: frame.sorting_key)
        self.arrange_activities()
        self.update_task_list()

    def remove_activity(self, frame):
        frame.grid_forget()
        self.completed.append(frame)
        self.activities.remove(frame)
        self.arrange_activities()
        self.update_task_list()

    def arrange_activities(self):
        for i, frame in enumerate(self.activities):
            frame.grid(row=i, column=1, sticky="ew")
    
    def get_priority_value(self, priority):
        priority_values = {
            "gray": 3,
            "blue": 2,
            "yellow": 1,
            "red": 0
        }
        return priority_values[priority]

    def update_task_list(self):
        # update canvas scroll region
        self.task_list_frame_inner.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))


class CalendarWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Calendar")
        self.geometry("300x250")
        self.minsize(300, 250)
        
        self.cal = Calendar(self, firstweekday="sunday", date_pattern="dd/mm/yyyy")
        self.cal.pack(pady=10)
        select_button = Button(self, text = "Get Deadline", command = self.get_deadline)
        select_button.pack()

    def get_deadline(self):
        date = self.cal.get_date()
        self.parent.deadline.set(date)
        self.destroy()


class MenuBar(Menu):
    def __init__(self, parent, stats, task_display):
        super().__init__(parent)
        self.parent = parent
        self.stats = stats
        self.task_display = task_display

        #file menu
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(label="Save", command=self.save_tasks)
        file_menu.add_command(label="Load", command=self.load_tasks)
        file_menu.add_command(label="Clear", command=self.confirm_clear_tasks)
        self.add_cascade(label="File", menu=file_menu)

        #statistics menu
        stats_menu = Menu(self, tearoff=0)
        stats_menu.add_command(label="General", command=self.show_general_stats)
        stats_menu.add_command(label="Priorities", command=self.show_priority_stats)
        stats_menu.add_command(label="Tags", command=self.show_tags_stats)
        self.add_cascade(label="Statistics", menu=stats_menu)

    def save_tasks(self):
        try:
            #extract data from self.activities and self.completed
            task_data = {
                "active": [],
                "completed": []
            }

            for frame in self.task_display.activities:
                task_data["active"].append({
                    "task": frame.task_label.cget("text"),
                    "deadline": frame.deadline_label.cget("text") if frame.deadline_label else "",
                    "priority": frame.prio,
                    "color": frame.task_label.cget("fg"),
                    "tags": frame.tags,
                })

            for frame in self.task_display.completed:
                task_data["completed"].append({
                    "task": frame.task_label.cget("text"),
                    "deadline": frame.deadline_label.cget("text") if frame.deadline_label else "",
                    "priority": frame.prio,
                    "color": frame.task_label.cget("fg"),
                    "tags": frame.tags,
                })

            #save to file
            with open("tasks.pkl", "wb") as file:
                pickle.dump(task_data, file)
            messagebox.showinfo("Save", "Tasks saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save tasks: {str(e)}")

    def confirm_clear_tasks(self):
        choice = messagebox.askyesno("Clear", "Are you sure you want to clear all tasks?")
        if choice:
            self.clear_tasks()

    def clear_tasks(self):
        self.task_display.activities.clear()
        self.task_display.completed.clear()
        self.task_display.task_list_frame_inner.destroy()
        self.task_display.task_list_frame_inner = Frame(self.task_display.canvas)
        self.task_display.task_list_frame_inner.pack(fill=BOTH, expand=True)
        self.task_display.canvas.create_window((0, 0), window=self.task_display.task_list_frame_inner, anchor=NW)

    def load_tasks(self):
        try:
            #load from file
            with open("tasks.pkl", "rb") as file:
                task_data = pickle.load(file)

            #clear existing data
            self.clear_tasks()

            #load completed tasks
            for task_info in task_data.get("completed", []):
                task = task_info["task"]
                deadline = task_info.get("deadline", "")
                prio = task_info["priority"]
                color = task_info["color"]
                tags = task_info["tags"]
                self.task_display.add_activity(task, prio, color, tags, deadline)
                self.task_display.remove_activity(self.task_display.activities[-1])

            #load active tasks
            for task_info in task_data.get("active", []):
                task = task_info["task"]
                deadline = task_info.get("deadline", "")
                prio = task_info["priority"]
                color = task_info["color"]
                tags = task_info["tags"]
                self.task_display.add_activity(task, prio, color, tags, deadline)
            
            messagebox.showinfo("Load", "File loaded successfully!")
        except FileNotFoundError:
            messagebox.showinfo("Load", "Saved file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load tasks: {str(e)}")

    def show_general_stats(self):
        general_stats = self.stats.get_general_stats()
        GeneralStatsWindow(self.parent, "General Statistics", general_stats)

    def show_priority_stats(self):
        prio_stats = self.stats.get_priority_stats()
        PriorityStatsWindow(self.parent, "Priority Statistics", prio_stats)

    def show_tags_stats(self):
        tags_stats = self.stats.get_tags_stats()
        TagsStatsWindow(self.parent, "Tags Statistics", tags_stats)


class StatisticsManager(object):
    def __init__(self, task_display):
        self.task_display = task_display

    def get_general_stats(self):
        active = len(self.task_display.activities)
        completed = len(self.task_display.completed)        
        total = active + completed

        return {
            "active": active, 
            "completed": completed, 
            "total": total
        }

    def get_priority_stats(self):
        prio_high = sum(1 for frame in self.task_display.activities if frame.prio == "red") 
        prio_high_complete = sum(1 for frame in self.task_display.completed if frame.prio == "red")
        prio_medium = sum(1 for frame in self.task_display.activities if frame.prio == "yellow") 
        prio_medium_complete = sum(1 for frame in self.task_display.completed if frame.prio == "yellow")
        prio_low = sum(1 for frame in self.task_display.activities if frame.prio == "blue") 
        prio_low_complete = sum(1 for frame in self.task_display.completed if frame.prio == "blue")
        prio_none = sum(1 for frame in self.task_display.activities if frame.prio == "gray") 
        prio_none_completed = sum(1 for frame in self.task_display.completed if frame.prio == "gray")

        return {
            "prio_high": prio_high, 
            "prio_high_all": prio_high + prio_high_complete,
            "prio_medium": prio_medium, 
            "prio_medium_all": prio_medium + prio_medium_complete,
            "prio_low": prio_low, 
            "prio_low_all": prio_low + prio_low_complete,
            "prio_none": prio_none, 
            "prio_none_all": prio_none + prio_none_completed,
        }

    def get_tags_stats(self):
        tag_personal = sum(1 for frame in self.task_display.activities if frame.tags["Personal"] == 1)
        tag_personal_all = sum(1 for frame in self.task_display.completed if frame.tags["Personal"] == 1)
        tag_family = sum(1 for frame in self.task_display.activities if frame.tags["Family"] == 1)
        tag_family_all = sum(1 for frame in self.task_display.completed if frame.tags["Family"] == 1)
        tag_friend = sum(1 for frame in self.task_display.activities if frame.tags["Friend"] == 1)
        tag_friend_all = sum(1 for frame in self.task_display.completed if frame.tags["Friend"] == 1)
        tag_work = sum(1 for frame in self.task_display.activities if frame.tags["Work"] == 1)
        tag_work_all = sum(1 for frame in self.task_display.completed if frame.tags["Work"] == 1)
        tag_entertainment = sum(1 for frame in self.task_display.activities if frame.tags["Entertainment"] == 1)
        tag_entertainment_all = sum(1 for frame in self.task_display.completed if frame.tags["Entertainment"] == 1)

        return {
            "tag_personal": tag_personal, 
            "tag_personal_all": tag_personal + tag_personal_all,
            "tag_family": tag_family, 
            "tag_family_all": tag_family + tag_family_all,
            "tag_friend": tag_friend, 
            "tag_friend_all": tag_friend + tag_friend_all,
            "tag_work": tag_work, 
            "tag_work_all": tag_work + tag_work_all,
            "tag_entertainment": tag_entertainment, 
            "tag_entertainment_all": tag_entertainment + tag_entertainment_all,
        }


class ToDoList(object):
    def __init__(self):
        root = Tk()
        root.title("To-do List")
        root.geometry("900x600")
        root.minsize(900, 600)

        #create margins
        margin_top = Frame(root, width=500, height=15)
        margin_left = Frame(root, height=300, width=15)
        margin_mid = Frame(root, height=300, width=15)
        margin_right = Frame(root, height=300, width=15)
        margin_bottom = Frame(root, width=500, height=15)
        margin_top.grid(row=1, column=1, columnspan=5)
        margin_left.grid(row=2, column=1, sticky=W)
        margin_mid.grid(row=2, column=3)
        margin_right.grid(row=2, column=5, sticky=E)
        margin_bottom.grid(row=3, column=1, columnspan=5)

        #expand margins
        root.grid_rowconfigure(1, weight=1)
        root.grid_rowconfigure(3, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(5, weight=1)

        #create main working frames
        self.task_creator = TaskCreator(root, self.create_activity)
        self.task_creator.grid(row=2, column=2, sticky=N)

        self.task_display = TaskDisplay(root)
        self.task_display.grid(row=2, column=4, sticky=N)

        self.statistics = StatisticsManager(self.task_display)
        self.menu_bar = MenuBar(root, self.statistics, self.task_display) 

        root.config(menu=self.menu_bar)

        root.mainloop()

    def create_activity(self, task, prio, color, tags, deadline):
        self.task_display.add_activity(task, prio, color, tags, deadline)


if __name__ == "__main__":
    ToDoList()
