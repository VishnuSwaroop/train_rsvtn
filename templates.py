
ALL_PAGE_HEADER = """\
<body bgcolor="#ffc34d">
<h1 align="center"><font color="993300">GT Train Reservation System</font></h1>
<p></p>
<h2 align="center">Team 45</h2>
<a href=/> <h3 align="left"> HOME </h3> </a>
<hr>
<hr>
</html>
"""

HOME_PAGE = """\
<body bgcolor="#ffc34d">
<h2 align="center">Login</h2>

<form action="/" method="post">
      <div>
        <label for="username">Username:</label>
        <input type="text" name="username" /> </div>
        <label for="password">Password:</label>
        <input type="text" name="password" /> </div>
        <div class="button"><button type="submit">Login</button></div>
        <a href=/register> <h3 align="left"> Register </h3> </a>
    </form>
</html>
"""

REG_PAGE = """\
<body bgcolor="#ffc34d">
<h2 align="center">Registration Page</h2>

<form action="/register" method="post">
      <div>
        <label for="username">Username:</label>
        <input type="text" name="username" /> </div>
        <p></p>
        <label for="email">Email:</label>
        <input type="text" name="email" /> 
        <p></p>
        <label for="password">Password:</label>
        <input type="text" name="password" /> </div>
        <p></p>
        <label for="conf_password">Confirm Password:</label>
        <input type="text" name="conf_password" /> </div>
        <div class="button"><button type="submit">Register</button></div>

    </form>
</html>
"""


MENU_PAGE = """\
<ul>
<li> <a href=/viewschedule><h3> View train schedule</h3></a>
<p></p>
<li> <a href=/makereserve><h3> Make a new reservation</h3> </a>
<p></p>
<li> <a href=/updatereserve> <h3> Update a reservation</h3> </a>
<p></p>
<li> <a href=/cancelreserve> <h3>Cancel a reservation </h3></a>
<p></p>
<li> <a href=/givereview> <h3>Give review </h3></a>
<p></p>
<li> <a href=/addschool> <h3>Add school info </h3></a>
</ul>
"""

SCHEDULE_PAGE = """\
<body bgcolor="#ffc34d">
<h2 align="center">Train Schedule</h2>

<form action="/viewschedule" method="post">
      <div>
        <label for="trainno">Train No :</label>
        <input type="text" name="trainno" /> </div>
        <div class="button"><button type="submit">Search</button></div>
        <a href=/menu> <h3 align="left"> Back </h3> </a>
    </form>
</html>
"""

SCHOOL_PAGE = """\
<body bgcolor="#ffc34d">
<h2 align="center">Add school info</h2>

<form action="/addschool" method="post">
      <div>
        <label for="schoolemail">Add school email :</label>
        <input type="text" name="schoolemail" /> </div>
        <p>Please enter the email address ending with .edu</p>
        <div class="button"><button type="submit">Submit</button></div>
        <a href=/menu> <h3 align="left"> Back </h3> </a>
    </form>
</html>
"""