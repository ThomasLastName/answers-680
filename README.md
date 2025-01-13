# MATH 680 ANSWERS TO EXERCISES IN LABS
These are the answers to the exercises presented in labs for the class MATH 680 at Texas A&M university, which can be found in my repo [labs_680](https://github.com/ThomasLastName/labs_680). I wrote these as the TA for the class in spring 2024.

---

# Installation/Upgrading

**Currently, installation requires that you have git installed on your machine!** (see also [#7](https://github.com/ThomasLastName/quality-of-life/issues/7))

For general users, the same command `pip install --upgrade git+https://github.com/ThomasLastName/answers-680.git` can be used for both installing and updating the code, along with all of its dependencies.

For developers, I recommend instead cloning the repo as normal, navigating to the root directory of the repo, and then using the command `pip install -e .` (the `-e` flag stands for "editable", and the `.` indicates the current working directory). This way, "if you update the code from Github [or locally], your installation will automatically take those changes into account without requiring re-installation" (explanation borrowed from [these docs](https://sepia-lanl.readthedocs.io/en/latest/)).
