# StudySync
The Study Phase Planner is an app designed to help students efficiently plan their study phases leading up to exams. Users input details such as exam dates, difficulty levels, available time, sleep requirements, travel time, and meal preferences. The app then generates a personalized study schedule, ensuring balanced preparation for each subject while taking into consideration personal needs. The goal is to create a flexible and adaptive study plan that maximizes productivity without compromising well-being. Just kidding there is no well-being at ETH. 

## How to Contribute
1. Clone the repository:  
   ```bash
   git clone git@gitlab.ethz.ch:abensland/studysync_app.git
   ```
   or with http:
   ```bash
   git clone https://gitlab.ethz.ch/abensland/studysync_app.git
   ```
2. Create a new branch for your tasks:  
   ```bash
   git checkout -b <branch-name>
   ```
3. Commit changes and push to the repository:  
   ```bash
   git add .
   git commit -m "Task description"
   git push origin <branch-name>
   ```

## If you don’t want to work on a branch, you shouldn’t change one of the main files directly! Create a new file, copy the code, and then make your changes in the new file. Otherwise, there will be merge issues when two people are working on the same file simultaneously.

### Virtual Environments (Optional, but Seriously, Just Do It)

Okay, so you don’t *have* to use a virtual environment, but trust me—when people are on different setups, **everything that can break will break**. Especially when someone checks out a different version of Python or some random package. If you don’t want that pain, here’s what to do:

1. **Set Up a Virtual Environment:**  
   Run this in the project folder:  
   ```bash
   python3 -m venv .venv
   ```

2. **Activate It:**  
   - Mac/Linux:  
     ```bash
     source .venv/bin/activate
     ```
   - Windows:  
     ```bash
     .venv\Scripts\activate
     ```

3. **Install Dependencies:**  
   Make sure you’re on the same page as everyone else:  
   ```bash
   pip install -r requirements.txt
   ```

4. **If You Add Stuff:**  
   Don’t forget to update `requirements.txt`:  
   ```bash
   pip freeze > requirements.txt
   ```

5. **Deactivate When You’re Done:**  
   ```bash
   deactivate
   ```

Not mandatory, but if you skip this and things break, don’t say we didn’t warn you! 😅