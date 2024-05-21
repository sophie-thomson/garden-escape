"""
Story text for Garden Escape: Honey I Shrunk the Coder!

This module contains all of the story narrative that sets the scene for the player's 
adventure. 

Each block of text has been declared as a variable. As the player chooses different 
options in the story, their choice will identify which variable (and which text) 
should be displayed to the player as they continue on their adventure.
"""

INTRO_TEXT = """
 You are working from home on your latest Python terminal project in the 
 garden thinking “This is what remote working is all about!” when you receive 
 a mysterious email featuring nothing but a big red button inviting you to 
 'Click Me'.

 You know you shouldn't...
 But curiosity gets the better of you and you click the button... 

 There is a flash and you suddenly find yourself standing amidst gigantic 
 blades of grass in a vast jungle filled with towering plants and hidden 
 dangers. With no idea how it happened, you slowly realise you are still in 
 your garden, but you are no bigger than a ladybug!

 Thankfully you still have your laptop with you, but there is no wifi. Your 
 only chance is to navigate through this treacherous landscape and get back 
 to your house to see if you can find a way to revert to your last save before 
 the corrupted email arrived."""

SPIDER_TEXT = """
 Determined to make it home and return to your normal size, you take a deep 
 breath and cautiously make your way through the 20ft tall grass.

 As you climb between some dandelions, you spot a massive spider hanging on 
 a thread, swaying gently in the shadows above your head.
"""

SPIDER_OPTION_A = " a) Try to sneak past the spider, hoping it doesn't notice you.\n"

SPIDER_OPTION_B = " b) Create a distraction so you can make a run for it.\n"

SPIDER_OPTION_A_TEXT = """
 You carefully manoeuver around the spider, hoping to avoid its notice. 
 However, your movement disturbs a nearby web strand, alerting the arachnid to 
 your presence. The spider fixes all 8 of its beady eyes on you and steadily 
 starts to descend..."""

SPIDER_OPTION_B_TEXT = """
 Remembering that you have your laptop with you, you use your coding skills to 
 hack into a nearby smart sprinkler, causing water to spray everywhere. You 
 are now soaking wet, but while the spider is distracted, you run for it and 
 escape into the undergrowth.
"""
NESTED_SPIDER_OPTIONS_TEXT = """
 You watch, transfixed in horror, as the spider stretches it's legs and drops
 towards you. 
 
 It seems to double in size as it gets closer and you can clearly
 see a pair of fangs glistening in the sunlight.

 You wish you had time to whip out your laptop and ask StackOverflow what to 
 do, but you need to act fast.

 Do you:\n"""

SPIDER_OPTION_A2 = " a) Quickly roll out of the way.\n"

SPIDER_OPTION_B2 = " b) Try to reason with the spider.\n"

SPIDER_OPTION_A2_TEXT = """
 You throw yourself across the ground and roll out of the way just in time, 
 narrowly avoiding the spider's deadly strike.

 Phew - that was close!

 Not stopping to check if the spider is in pursuit, you get to your feet and
 run in the direction of the house as fast as you can, stumbling and tripping 
 over roots and dirt piles until your chest feels like it's going to burst. 

 Looking around, there is no sign of the spider behind you, so you stop 
 running. 
 
 Doubled over and gasping for breath, you vow to get up early and 
 hit the gym more often if you ever make it out of this mess.
"""

SPIDER_OPTION_B2_TEXT = """
 Using a combination of hand gestures, foot tapping, and drawing in the dirt, 
 you attempt to reason with the spider, explaining your situation as a 
 shrunken developer just trying to get home.

 Surprisingly, the spider seems to understand and lets you pass unharmed. 

 You breathe a sigh of relief and hurry away, vowing that you will never harm 
 a spider again when you get back to normality."""

CENTIPEDE_STORY_TEXT = """
 Having made it past the spider, you feel pretty good about your progress, but 
 you are getting hungry. You think dreamily of your stash of trail mix and 
 chocolate buttons that keep you going through those long hours of debugging.
 
 You wonder if you'll ever get to use your 'World's #0 Programmer' mug again.

 Lost in your thoughts, you don't notice a movement in the house-sized plant 
 pots up ahead.

 Suddenly a gigantic centipede as long as a street lamp scuttles out from 
 behind your favourite glazed blue pot. You watch in terror as it meanders 
 fluidly around some pebbles and stops directly in your path.
"""

CENTIPEDE_OPTIONS_TEXT = """
 Your heart pounding with adrenaline, you square up against the centipede, 
 ready to defend yourself. 

 It hisses menacingly and raises the front of its body to loom above you, 
 its numerous legs poised to strike...

 Do you:
"""

CENTIPEDE_OPTION_A = " a) Attempt to outmaneuver it with your agility.\n"
CENTIPEDE_OPTION_B = " b) Search for a nearby object to use as a weapon.\n"

CENTIPEDE_OPTION_A_TEXT= """
 You weave left and right before darting between its legs, but the centipede 
 has lightning-fast reflexes and as it traps you in its claws, you feel your 
 body stiffen as the venom enters your bloodstream.

 Will you escape?
"""
CENTIPEDE_GAME_OVER_TEXT = """ 
 Sadly not. The centipede is not letting you go and the last thing you see 
 is a pair of glistening mandibles reaching hungrily towards your face.
 """

CENTIPEDE_OPTION_B_TEXT= """
 You look around frantically for something you can use as a weapon against 
 the centipede. Remembering your laptop, you open it up and turn the screen 
 brightness up to blinding, thrusting it towards the centipede's head and 
 shouting at the top of your voice. 

 Startled by the sudden movements, noise and bright light, the centipede 
 slinks away, allowing you to pass.
"""

RAKE_STORY_TEXT = """
 You push onwards towards the huge silhouette of your house, but you are 
 exhausted and starving and the sun is getting lower in the sky. You shudder 
 to think what it would be like to be stuck out here at night! 

 As you get closer to the back of your house, you start to think you might 
 actually make it through this nightmare if you can just figure out how on 
 earth to get in through the back door.

 You think you may have left the back door ajar, but you can't quite tell 
 from this distance over the top of the huge plants and leaves. While you 
 are pondering your next move, you have forgotten all about the rake propped 
 against your back door.
"""

RAKE_OPTIONS_TEXT = """
 A sudden gust of wind swings the door open, sending the rake tumbling 
 towards you!

 Do you:
"""

RAKE_OPTION_A = " a) Run back the way you came, losing ground but hopefully avoiding\n the path of the falling rake.\n"
RAKE_OPTION_B = " b) Watch the rake fall, trying to judge its trajectory before choosing\n which direction to jump in.\n"

RAKE_OPTION_A_TEXT = """
 You race through the grass away from the house, watching the shadow of the 
 rake grow around you as it hurtles towards you. 
 
 You can see sunlight on the ground ahead beyond the reach of the rake's
 shadow. If you can keep going, you might just do it!
"""
RAKE_GAME_OVER_TEXT = """
 Just when you think you're safe, you hear a flurry of feathers and only 
 have time to register the light reflecting on the huge sharp beak before 
 you are snatched up and swallowed whole.
"""

RAKE_OPTION_B_TEXT = """
 Miraculously, you narrowly avoid the rake's deadly prongs and long handle as 
 they come crashing to the ground. However, the impact of the fall has flung 
 you into the air and you are now hurtling towards your kitchen!
"""

NESTED_RAKE_OPTIONS_TEXT = """
 Thankfully you can see that the kitchen door is wide open and you are flying 
 straight towards it, but at this rate you will be hitting the kitchen 
 cupboard with enough force to cause some serious injuries!

 Do you:
"""

RAKE_OPTION_A2 = " a) Open up your laptop and hold it above your head hoping it\n will work as a glider.\n"
RAKE_OPTION_B2 = " b) Tuck your knees up to your chest ready to perform a stunt\n roll onto the kitchen floor.\n"

RAKE_OPTION_A2_TEXT = """
 Amazingly your trusty laptop catches the breeze and lifts you higher into the
 air before dropping you with an undignified bump onto the kitchen worktop.

 You lay there, dazed for a moment catching your breath as it dawns on you 
 that you have finally made it home!

 Heart racing, you open your laptop to check if it's still working. You 
 are beyond relieved to see your home screen jump to life, and you waste no 
 time connecting to the wifi and drilling down through your settings to roll 
 back to your last backup before the email.
"""

RAKE_OPTION_B2_TEXT ="""
 Well your stunt training might have worked if not for a passing Magpie!

 You hear a flurry of feathers, but before you can look round a sharp beak 
 snatches you up and swallows you up in one gulp.
"""
CONGRATULATIONS_TEXT = """
 At that moment, your neighbour arrives at your back door to return the drill 
 they borrowed. Staring at you quizzically, they are clearly wondering why 
 you are sitting on your worktop covered in mud, scratches and grass stains!

 Glancing at your grazed knees, you throw your head back and laugh until tears 
 roll down your cheeks. Your neighbour quietly crosses the kitchen and puts the 
 kettle on...
"""
