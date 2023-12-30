# Declare characters used by this game.
define e = Character("Emily", color="#c8ffc8", image="emily")
define v = Character("Veterinarian", color="#ffffc8", image="veterinarian")
define p = Character("Public Health Official", color="#c8c8ff", image="public_health")
define w = Character("Wildlife Expert", color="#ffc8c8", image="wildlife_expert")
define m = Character("Mom", color="#ff8c8c", image="mom")
define b = Character("Biology Teacher", color="#8c8cff", image="biology_teacher")
define wv = Character("Sanctuary vetrenarian", color="#8c8cff", image="Sanctuary vetrenarian")
define co = Character("Captain One Health", color="#8c8cff", image="captain_one_health")
define sm = Character("Salmonella Marauder", color="#ff8c8c", image="salmonella_marauder")
#images
image e  = "e.png"
image co = "co.png"
image sm = "sm.png"

# The game starts here.
label start:
    scene bg title_screen
    "Songbird Mystery: An Inquisitive Journey"
    "Emily, a young bird enthusiast, discovers her pet songbird, Luna, looking unwell. She decides to uncover the truth behind Luna's illness."
    "Chapter 1: A Concerning Change"
    scene bg emily_room
    show e at center
    e "I've been hearing a lot about Salmonella in Birds, I better make sure i learn more about it, so i can care best for Luna."

    # Present the player with choices.
    menu:
        "Consult a local veterinarian.":
            jump veterinarian_consultation
        "Start researching online.":
            jump online_research
        "Talk to Mom for advice.":
            jump mom_advice
        "Visit a local bird sanctuary for insights.":
            jump bird_sanctuary_visit
        "Join a local bird lovers' community group.":
            jump community_group

#mom advice
label mom_advice:
    scene bg emily_computer
    show m
    m "It is always good to ask a trusted adult if you are unsure of how to take care of your pets, "
    m "It is always critical to research proper sources or if unsure consult a Vet when it comes to animal healthcare"

#mom advice menu
    menu:
        "Consult a local veterinarian.":
            jump veterinarian_consultation
        "Start researching online.":
            jump online_research
        "Visit a local bird sanctuary for insights.":
            jump bird_sanctuary_visit
        "Join a local bird lovers' community group.":
            jump community_group

# The game starts here.
    scene bg title_screen
    "Songbird Mystery: An Inquisitive Journey"
    "Emily, a young bird enthusiast, discovers her pet songbird, Luna, looking unwell. She decides to uncover the truth behind Luna's illness."
    "Even though Luna recovers eventually, Emily decides that better understanding of bird health is critical for the long-term welfare of her pet."
    "Chapter 1: A Concerning Change"
    scene bg emily_room
    show e at center
    e "Luna has been less active lately and isn't singing as much. What should I do?"

    # Present the player with expanded choices.
    menu:
        "Consult a local veterinarian.":
            jump veterinarian_consultation
        "Start researching online.":
            jump online_research
        "Talk to Mom for advice.":
            jump mom_advice
        "Visit a local bird sanctuary for insights.":
            jump bird_sanctuary_visit
        "Join a local bird lovers' community group.":
            jump community_group
            
    #vet discussion         
label veterinarian_consultation:
    scene bg vet_office
    show e at left
    show v at right
    v "Welcome, Emily. How can I assist you with Luna today? There are several areas we can discuss to ensure her well-being."
    
    # Presenting choices for Emily.
    menu:
        "Discuss Luna's dietary habits.":
            jump vet_diet_discussion
        "Talk about Luna's environment and its impact.":
            jump vet_environment_discussion
        "Inquire about common bird diseases and prevention.":
            jump vet_disease_inquiry
        "Learn about the One Health approach.":
            jump vet_one_health_discussion

    # After

    v "Hello, Emily. What's troubling Luna?"
    e "She's less active and not eating well. Could it be serious?"
    v "Let's run some tests. Meanwhile, tell me about her diet and environment."
    e "Her diet hasn't changed, but she seems different."
    v "There are numerous reasons a bird can be sick, but in most cases the issues for indoor birds are minor."
    v "However, it is important to understand birds are highly sensitive to their environment."
    e "I understand, that's why I keep Luna indoors."
# Captain One Health's notes
show co at left
e " "  # This is a workaround to introduce Captain One Health's dialogue.
co "Excellent decision, Emily! Consulting a veterinarian is a wise choice. It exemplifies the One Health approach, which emphasizes the interconnectedness of human, animal, and environmental health. By seeking professional advice, you're not only addressing Luna's immediate needs but also considering broader health implications. Birds, like all animals, are integral parts of our ecosystem. Their health can be influenced by various factors, including nutrition, living conditions, and even human activities. A veterinarian's expertise helps ensure Luna's well-being while also contributing to a greater understanding of avian health. This holistic approach is crucial for maintaining balance in our natural world and preventing health issues that can cross between animals and humans."

# Salmonella Marauder's reaction
show sm at right
e " "  # This is a workaround to introduce Salmonella Marauder's dialogue.
sm "Drats! I was hoping for a misstep. But fear not, there are still many challenges ahead!"

# Return to the veterinarian conversation
show v at right  # Adjust 'at right' as needed for your scene
v "Keeping Luna indoors is a good start. Let's also explore her diet and any recent changes in her environment or routine."


# [Continue with veterinarian consultation]
label vet_diet_discussion:
    # Discussing Luna's dietary habits with One Health insights
    v "Let's discuss Luna's diet. What does she typically eat?"
    e "She usually has a mix of seeds and fruits. I occasionally give her some special bird treats."
    v "A varied diet is crucial. However, it's not just about variety. The quality and source of the food are also important. Have you considered incorporating fresh vegetables or cooked grains?"
    e "I haven't, actually. Which vegetables would you recommend?"
    v "Leafy greens like spinach and kale are great. You can also try bell peppers, carrots, and peas. Ensure they're fresh and thoroughly washed to avoid any pesticides, which can harm not just Luna but also the environment."
    show co at left
    co "Rightly said! The choice of Luna's diet reflects on the larger environmental health. Fresh and sustainably sourced food reduces environmental impact and supports a sustainable ecosystem."
    hide co
    e "That makes sense. What about grains?"
    v "Cooked brown rice or quinoa can be a nutritious addition. It's about creating a balance. Too much of anything, even good food, can lead to health issues. A balanced diet contributes to Luna's health and reduces the ecological footprint of her food."
    show co at left
    co "Exactly, Emily. The One Health approach is all about finding that balance. It's a holistic view that connects Luna's health to broader environmental and nutritional considerations."

label vet_environment_discussion:
    scene bg vet_office
    show e at left
    show v at right
    v "Let's discuss Luna's living environment. Birds are quite sensitive to their surroundings. Is her cage in a suitable location?"
    e "It's near the window. She enjoys the view, but could it be too drafty or noisy?"
    v "Placement is key. Birds thrive in a calm, stable environment, away from direct sunlight, loud noises, and strong odors. Also, how often do you clean her cage?"
    e "Once a week. Should I do it more frequently?"
    v "Yes, daily cleaning is crucial to prevent harmful bacteria build-up. Ensure her cage is spacious for free movement."
    # Captain One Health's notes
    show co at left
    co "Emily's attention to Luna's environment underscores a vital One Health principle. The health of our pets is deeply intertwined with their habitats. By ensuring a clean, safe, and comfortable environment for Luna, Emily is also contributing to a healthier, more sustainable world. Using eco-friendly cleaning products and maintaining a toxin-free space not only benefits Luna but also minimizes environmental impact"

label vet_disease_inquiry:
    scene bg vet_office
    show e at left
    show v at right
    v "It's crucial to be aware of common bird diseases. Has Luna shown any signs of respiratory distress, changes in droppings, or feather loss?"
    e "No, she hasn't. However, I'm concerned about the possibility of infections or parasites."
    v "That's a valid concern. Birds are vulnerable to various infections and parasites, both internal and external. Regular check-ups and maintaining a clean environment are essential for prevention."
    e "I will ensure she gets regular check-ups. Are there any preventive treatments you recommend?"
    v "Yes, there are several safe and effective treatments. I'll provide detailed information about them."
    e "Thank you. I'm committed to keeping Luna healthy."
    # Captain One Health's notes
    show co at left
    co "Emily's proactive approach to disease prevention in Luna is a key aspect of the One Health concept. By preventing diseases in birds, we also safeguard human health and the environment. Many avian diseases have the potential to affect humans and other animals. Thus, regular health check-ups, vaccinations, and preventive treatments are not just about caring for Luna but also about protecting our wider community and ecosystem from potential health risks. This integrated approach is at the heart of One Health, where animal health is seen as an integral part of public health."
    
    # Return to the previous menu or proceed to the next part of the story
    menu:
        "Return to previous topics.":
            jump veterinarian_consultation
        "Continue with the consultation.":
            jump vet_next_steps

# General Discussion on One Health
label vet_one_health_discussion:
    scene bg vet_office
    show e at left
    show v at right
    e "I've heard about the One Health approach. Can you tell me more about it and how it relates to Luna's health?"
    v "Certainly, Emily. One Health is a concept that recognizes the interconnection between animal health, human health, and our environment. It's about understanding that our health is tied to the health of animals and the world we share."
    v "In Luna's case, ensuring her health means understanding her diet, environment, living conditions, and even how these factors relate to broader ecological and public health issues."
    # Captain One Health's elaboration
    show co at left
    co "Emily, embracing One Health means recognizing that the choices we make in caring for Luna have wider implications. By ensuring her well-being, we're also contributing to a healthier environment and community. It's about preventing diseases, promoting sustainability, and understanding our role in the natural world."
    # Salmonella Marauder's comment
    sm "Bah, this One Health approach thwarts my efforts to spread disease and discord! Educated decisions and holistic thinking are my nemeses!"

    # Return to the previous menu or proceed to the next part of the story
    menu:
        "Return to previous topics.":
            jump veterinarian_consultation
        "Continue with the consultation.":
            jump vet_next_steps

label vet_next_steps:
    # Concluding the veterinary consultation
    # [Concluding dialogue]
    menu:
        "Go back to discuss more with the veterinarian.":
            jump veterinarian_consultation
        "Continue with Luna's care plan.":
            jump expert_blogs


label expert_blogs:
    # Emily browses expert blogs, evaluating their credibility.
    scene bg emily_computer
    e "Let's see what these blogs say. But I must check their credibility first."
    m "Emily, it's good to read blogs, but always cross-check their information with scientific sources."
    e "You're right, Mom. I'll make sure to verify the information I find."
    show co at left
    co "That's a smart approach, Emily. In an era of misinformation, cross-verifying facts is key to One Health."
    sm "Curses! Your diligence in seeking credible information foils my plans."
    # Captain One Health's comments
    show co at left
    co "Emily, your commitment to Luna's comprehensive care reflects the One Health philosophy perfectly. The steps you're taking with Luna not only address her individual health but also contribute to the broader goal of understanding and preventing diseases that can impact birds, humans, and our shared environment. Your efforts exemplify the interconnectedness of all health domains."

    # Salmonella Marauder's reaction
    sm "Hmph, your diligence in Luna's care and the application of this One Health approach hinders my plans. But beware, challenges still await you and Luna. I thrive in the complexities and unpredictability of health and the environment!"


# Further sections for online research, mom's advice, bird sanctuary visit, and community group will be similarly expanded with rich dialogue and multiple options. Each option will lead to a detailed discussion or exploration, providing the player with a wealth of information and choices to influence the story.
    # Option to return to other resources
    menu:
        "Explore other online resources":
            jump start_online_research

# The same level of detail and depth will be applied to the rest of the game, ensuring a rich and immersive experience for the player.

label start_online_research:
    scene bg emily_computer
    e "The internet is a vast resource for information. It’s time to do some research on bird health, but I must be cautious about where I get my information."

    menu:
        "Investigate scientific research on avian health.":
            jump scientific_research
        "Examine academic journals and papers on bird health.":
            jump academic_papers
        "Browse expert blogs on bird care, assessing their credibility.":
            jump expert_blogs
        "Navigate social media for bird health information, cautiously.":
            jump social_media

label online_research:
    scene bg emily_computer
    e "The internet is a vast resource, but I need to be careful about the information I find. It's crucial to rely on trustworthy and scientific sources for Luna's health."

    menu:
        "Investigate scientific research on avian health.":
            jump scientific_research
        "Examine academic journals and papers on bird health.":
            jump academic_papers
        "Browse expert blogs on bird care, assessing their credibility.":
            jump expert_blogs
        "Check Social Media for information on Bird Care":
            jump social_media

label scientific_research:
    # Emily delves into scientific research on bird health.
    scene bg emily_computer
    e "These scientific studies offer detailed insights into avian health. It's important to understand the science behind bird care."
    show co at left
    co "Emily, diving into scientific research is a wise move. Reliable, peer-reviewed studies provide accurate information, crucial in making informed decisions for Luna's health."
    hide co
    show sm at right
    sm "I despise accurate information! It disrupts my plans to spread misconceptions."
    hide sm
    # Option to return to other resources
    menu:
        "Explore other online resources":
            jump online_research
    # Option to return to other resources
menu:
        "Explore more online resources.":
            jump start_online_research
        "Proceed to the next part of your research.":
            jump bird_sanctuary_visit

label academic_papers:
    # Emily explores academic journals and papers about birds.
    scene bg emily_computer
    e "Academic journals are treasure troves of verified information. It's fascinating to learn from these comprehensive studies."
    show co at left
    co "Excellent choice, Emily. Academic papers are the backbone of informed understanding, crucial in applying One Health principles effectively."
    show sm at right
    sm "Academic rigor? How boring! My deceptions thrive in ignorance."
    co "and that is why you will never win, as long as science based practices are employed, and information from research is applied, we can fight against all diseases."
    # Option to return to other resources
menu:
        "Explore more online resources.":
            jump start_online_research
        "Proceed to the next part of your research.":
            jump bird_sanctuary_visit

    # Emily browses expert blogs, evaluating their credibility.
label social_media: 
    scene bg emily_computer
    e "Let's see what these blogs say. But I must check their credibility first."
    m "Emily, it's good to read blogs, but always cross-check their information with scientific sources."
    e "You're right, Mom. I'll make sure to verify the information I find."
    show co at left
    show sm at right
    co "That's a smart approach, Emily. In an era of misinformation, cross-verifying facts is key to One Health."
    sm "Curses! Your diligence in seeking credible information foils my plans."

#Menu for navigating from the social media section
menu:
        "Explore more online resources.":
            jump start_online_research
        "Proceed to the next part of your research.":
            jump bird_sanctuary_visit

    # Option to return to other resources  
menu:
        "Investigate scientific research on avian health.":
            jump scientific_research
        "Examine academic journals and papers on bird health.":
            jump academic_papers
        "Browse expert blogs on bird care, assessing their credibility.":
            jump expert_blogs

menu:
        "Revisit some online resources.":
            jump start_online_research
        "Proceed to the next step in Luna’s care.":
            jump bird_sanctuary_visit  # Replace 'next_section' with the appropriate label for the next part of the game.

label bird_sanctuary_visit:
    scene bg bird_sanctuary
    show e at left
    show w at right
    e "This sanctuary is teeming with life. I'm eager to learn more about how to care for Luna and understand her needs in relation to the wider ecosystem."

    show w
    w "Welcome, Emily! I'm Jordan, a wildlife expert. Let's explore how we can help Luna and understand her role in the greater environmental context."
    # ... [Continue with discussion on diet, environment, and the broader ecological implications of Luna’s care]
menu:
        "Explore more in the sanctuary.":
            jump start_bird_sanctuary_visit
        "Proceed to the next part of the story.":
            jump start_community_group

label Sanctuary_vet_center:
    scene bg bird_sanctuary
    show e at center
    e "I'm hoping the sanctuary's experts can offer deeper insights into Luna's condition, especially in the context of her natural environment and broader ecological health."

    menu:
        "Consult with the sanctuary's avian veterinarian.":
            jump sanctuary_vet
        # ... [Include other options like health workshop, bird observation, and behavior specialist]

menu:
        "Explore more in the sanctuary.":
            jump start_bird_sanctuary_visit
        "Proceed to the next part of the story.":
            jump start_community_group
label start_bird_sanctuary_visit:
    scene bg bird_sanctuary
    e "I'm at the bird sanctuary to learn more about Luna's health in a broader ecological context. What should I explore first?"

    menu:
        "Consult with the sanctuary's avian veterinarian.":
            jump sanctuary_vet
        "Join a bird health workshop.":
            jump health_workshop
        "Observe and learn from the birds in the sanctuary.":
            jump bird_observation
        "Talk to a bird behavior specialist.":
            jump behavior_specialist

# Consulting the Sanctuary Veterinarian
label sanctuary_vet:
    scene bg sanctuary_vet_office
    show e at left
    show wv at right
    e "I'm here to get insights on Luna's condition from a bird health expert."
    wv "Let's talk about Luna's symptoms and what they could indicate about her health and the environment."
    # [Detailed consultation about Luna's health]

    sm "Knowledgeable veterinarians make my job harder. They connect the dots between individual health and the environment!"

    # Return to the sanctuary start menu
    menu:
        "Explore more options in the sanctuary.":
            jump start_bird_sanctuary_visit
        "Proceed to the next part of Emily's journey.":
            jump start_community_group

# Bird Health Workshop
label health_workshop:
    scene bg bird_sanctuary
    e "I'm attending a workshop about bird health. This should be educational."
    # [Emily learns about various aspects of bird health]
    
    co "Workshops are great for gaining comprehensive knowledge, Emily. It's all part of understanding One Health."

    # Return to the sanctuary start menu
    menu:
        "Explore more options in the sanctuary.":
            jump start_bird_sanctuary_visit
        "Proceed to the next part of Emily's journey.":
            jump start_community_group

# Bird Observation
label bird_observation:
    scene bg bird_sanctuary
    e "Observing birds in their natural habitat can teach me a lot."
    # [Emily observes different birds, learning about their behaviors and environment]

    co "Direct observation is a key way to learn, Emily. It helps connect Luna's behavior to what's natural for birds."

    # Return to the sanctuary start menu
    menu:
        "Explore more options in the sanctuary.":
            jump start_bird_sanctuary_visit
        "Proceed to the next part of Emily's journey.":
            jump start_community_group

label end_bird_sanctuary_visit:
    e "My visit to the sanctuary has been enlightening. What should I do next?"
    menu:
        "Revisit some sections in the sanctuary.":
            jump start_bird_sanctuary_visit
        "Proceed to the next step in helping Luna.":
            jump start_community_group  # Replace 'next_section' with the label for the next part of the game.


#### Community Group Interaction

label start_community_group:
    scene bg community_center
    e "I'm here to engage with other bird lovers and learn about community and environmental health. Where should I start?"

    menu:
        "Share experiences with the group.":
            jump group_discussion
        "Attend a talk by a bird health expert.":
            jump expert_talk
        "Participate in a group bird-watching activity.":
            jump bird_watching
        "Seek advice from experienced bird owners.":
            jump owner_advice

# Group Discussion
label group_discussion:
    scene bg community_center
    e "I'm curious to hear other bird owners' experiences and share my own story about Luna."
    # [Emily interacts with the group, shares experiences, and learns from others]
    show co at left
    co "Engaging with a community is a vital aspect of One Health. Shared experiences can provide valuable insights into bird care and health."
    hide co 
    show sm at right
    sm "Community wisdom, huh? It might be harder to spread misinformation here."
    hide sm
    # Return to the community group menu
    menu:
        "Explore other activities at the community center.":
            jump start_community_group
        "Continue with the next part of Emily's journey.":
            jump chapter_conclusion

# Expert Talk
label expert_talk:
    scene bg community_center
    e "I'm excited to learn from a bird health expert. This talk should be very informative."
    # [Emily attends the expert talk, learning about the latest in avian health]
    show co at left
    co "Knowledge is key, Emily. Expert insights can significantly enhance your understanding of avian health."
    hide co
    show sm at right
    sm "Experts and their facts! They make my job more difficult."

    # Return to the community group menu
    menu:
        "Explore other activities at the community center.":
            jump start_community_group
        "Continue with the next part of Emily's journey.":
            jump chapter_conclusion

# Bird Watching Activity
label bird_watching:
    scene bg community_center
    e "Bird watching with a group will be a great way to observe bird behavior in a natural setting."
    # [Emily participates in bird watching, learning about different species and their behaviors]
    show co at left
    co "Observation in nature is a great way to connect with the environment and understand bird behavior."
    hide co
    sm "Enjoy your bird watching, Emily. But remember, not all lessons are learned in the field."
    hide sm
    # Return to the community group menu
    menu:
        "Explore other activities at the community center.":
            jump start_community_group
        "Continue with the next part of Emily's journey.":
            jump chapter_conclusion

# Advice from Experienced Bird Owners
label owner_advice:
    scene bg community_center
    e "I hope to gain some practical tips and advice from experienced bird owners."
    # [Emily speaks with experienced bird owners, gaining practical advice and tips]
    show co at left
    co "Practical experience is invaluable, Emily. Learning from others who have cared for birds can offer you practical and effective solutions."
    hide co
    sm "Practical advice can be useful, but beware, not all advice is good advice."
    hide sm
    # Return to the community group menu
    menu:
        "Explore other activities at the community center.":
            jump start_community_group
        "Continue with the next part of Emily's journey.":
            jump chapter_conclusion

# [Include any additional content, side stories, or educational elements as desired]
label community_group:
    scene bg community_center
    show e at center
    e "Engaging with fellow bird enthusiasts could offer new perspectives on Luna's health and its connection to community and environmental health."

    menu:
        "Share experiences with the group.":
            jump end_community_group
        # ... [Include other options like expert talk, bird-watching, and owner advice]

label end_community_group:
    e "This community group has offered diverse perspectives on bird health. What's my next step for Luna?"
    menu:
        "Move forward with Luna's care plan.":
            jump chapter_conclusion  # Replace 'next_section' with the label for the next part of the game.

# Conclusion of the Current Chapter
label chapter_conclusion:
    scene bg emily_room
    show e at center
    e "After consulting the veterinarian, researching online, visiting the bird sanctuary, and talking with the community group, I've learned so much about bird health and the One Health approach. It's time to apply this knowledge to help Luna."

    # Captain One Health's closing remarks
    show co at left
    co "Well done, Emily! You've taken a comprehensive approach to Luna's health, considering not just her immediate needs but also the broader environmental and public health aspects. This journey has been a testament to the One Health concept, demonstrating how interconnected our world is."

    # Salmonella Marauder's final grumble
    show sm at right
    sm "You may have won this round, Emily, but the challenge of maintaining health in a complex world continues. I'll be watching!"

    # Emily's resolution
    e "Thanks to everyone's help, I feel more confident in caring for Luna and making informed decisions. I know there's still a lot to learn, but I'm ready for the challenge."

    # Transition to the next chapter or conclusion
    menu:
        "Start the next chapter in Emily's journey.":
            jump next_chapter  # Replace 'next_chapter' with the label for the next chapter
        "End the current session.":
            jump end_game

# End of the game session
label end_game:
    scene bg end_screen
  
    "Thank you for playing Songbird Mystery: An Inquisitive Journey. Your journey with Emily and Luna doesn't have to end here. Keep exploring, learning, and growing. Until next time!"

    return  # This returns to the game menu or exits the session

# [If there's a next chapter, its content goes here]
label next_chapter:
    # Content for the next chapter of Emily's journey
    # ...

    # [Continue with the story]

# [Include any additional game mechanics, side stories, or educational content as needed]
