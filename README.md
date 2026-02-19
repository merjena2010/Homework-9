
Homework 2: Reflection Answers
1. How does the POST route process form data?
In my app, when a user fills out the name and message boxes and clicks "Post," the browser sends that data to the server. My Flask route uses request.form.get to grab the name and the message. It then puts them into a dictionary and adds it to the list of messages so it can be displayed on the page.
2. How did you implement delete functionality?
I gave every message its own unique ID number. I created a special "Delete" link for each message. When you click it, it sends that message's ID to a specific route in Python. Python then looks through the list, removes the message that matches that ID, and saves the new list back to the file.
3. What file operations did you use?
I used the JSON module to save the data. I used json.load to read the messages from the file so they appear when the page opens. I used json.dump to save the data whenever a new message is added or one is deleted. This way, the messages don't disappear when I restart the app.
4. What was your biggest challenge?
The hardest part was making sure the app didn't crash if the messages.json file was missing or empty. I had to write a special check to see if the file existed first. If it didn't exist, I told Python to just start with an empty list.
5. How did AI help you?
AI helped me design the CSS so the guest book looks like a tennis court (green and yellow colors). It also helped me fix an error I had with the "Delete" route where the ID wasn't being recognized as a number.