Home Route (/): This is the main landing page. It uses a variable to greet me by name and introduces the website.

About Route (/about): This page displays a paragraph about who I am (a 15-year-old tennis player) and my interest in coding.

Hobbies Route (/hobbies): This page displays a list of my favorite activities. It uses a loop to generate a list of items dynamically.

2. How did you pass data to templates?
I passed data using keyword arguments inside the render_template function.

For the Home and About pages, I passed single string variables (e.g., name="Merjen").

For the Hobbies page, I passed a Python List object. In the HTML template, I used a Jinja2 {% for %} loop to iterate through the list and display each hobby as a <li> item.

3. What was challenging about Flask?
The most challenging part was setting up the folder structure correctly. At first, my CSS wouldn't load because I didn't realize it had to be inside a folder named static. I also had to learn how to use url_for in my HTML to link the stylesheet properly so that the design would show up on every page.


Home Page (Showing your name)

About Page (Showing your bio)

Hobbies Page 
