Dawson Lakes, CJ Spencer

**Google Doc Link**: https://docs.google.com/document/d/1Dl1AVSDr4NsXqB4LCj3x80LPWYMP8NgYPWeCkpAiT1M/edit?usp=sharing

---
 
# https://stackoverflow.com/questions/70058132/how-do-i-make-a-timer-in-python
# https://stackoverflow.com/questions/46312470/difference-between-methods-and-attributes-in-python
# https://stackoverflow.com/questions/23703863/in-python-is-object-equal-to-anything-besides-itself
# https://stackoverflow.com/questions/51342774/how-to-flip-image-with-opencv-and-python-without-cv2-flip
# https://www.geeksforgeeks.org/how-to-move-your-game-character-around-in-pygame/

Catch A Crop

A game that will catch falling fruit until failure from which the game will close. Everytime you collect fruit you will receive one point, points will collect in bottom or top right of the screen showing you how many fruit you have caught.

**Source Assignment(s)**: `T011, H09, and T012

**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:




Use the left and right arrow keys to move your character left and right. Fruit will fall from the tree. You must catch the
fruits before they hit the ground. If you catch a fruit, you will gain 1 point. If you miss, you will lose a life and the
respect of your fellow orchard co-workers. When the game is lost, you will be prompted to press r to restart and try again,
or q to quit the game and end the program.

### ❗Errors and Constraints
Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

The only bug we have found is that the there is no border wall stopping the player. This, the player can move off-screen.
He can return if you press the key facing the opposite direction, but the player will go off-screen if the user chooses.

### ❗Reflection
In three to four well-written paragraphs, address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- (For partners) How well did you work with your partner? What made it go well? What made it challenging?

    We selected our project because we wanted to create a game. Gaming is always a fun project that serves the simple purpose
of entertainment. Despite the gameplay of our game being simple, the work that went into it was lesser so. It took a while
to get certain aspects working, but we are happy with what we have accomplished. A catch game is simple to explain,
and it is familiar to many gamers as a "classic" retro game.
    We learned that even simple designs can be difficult if the developers want to add in more things or fix bugs. There 
are so many unforeseen issues that can come up both as runtime errors and semantics. We learned that dual programming 
makes this grueling process so much more bearable. 
    The hardest part of this project was debugging. We struggled with getting things to operate on time and player input
rather than ticks entire frame by frame based upon user input. We had an issue where the screen would only update or move
each time the user clicked in a key. So, the user would have to click constantly to keep the game moving. Another issue 
was that the player would move consistently, but the fruits would fall at the same rate as the player rather than 
periodically falling based upon a constant timer. 
    I had a great time working with my partner. We shared the same device for most of the programming to both stay focused
on the same area, thus, most of the commits came from CJ's device(me). The only challenges were finding effective times 
where we could work outside of class. We most contributed very important updates to the program, and we are both satisfied
for the most part with how it came out. Although, we do wish we could have implemented a few other things such as a danger
object to avoid.