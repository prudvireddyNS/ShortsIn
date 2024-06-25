from langchain.prompts import PromptTemplate

# script_template = """Create a story for YouTube Shorts. The story should be engaging, concise (up to 60 seconds), and include a hook, main content, and a call-to-action (CTA). Use the information provided below to generate the script. Make sure to use a conversational and energetic tone suitable for a broad audience.

# **Title:** [Title of the Short]
# **Description:** [Brief description of the video]
# **Tags:** [Relevant tags]

# **Topic Text:**
# {topic}

# **story:**

# **[0-5 seconds]:** [Hook - an engaging introduction to capture viewers' attention]
# [Main Content Part 1 - present the first main point]
# [Main Content Part 2 - present the second main point]
# .
# .
# [Main Content Part n - present the nth main point]
# **[55-60 seconds]:** [Call-to-action - prompt viewers to like, comment, and subscribe]

# Make sure the script is punchy, direct, and visually descriptive to align with the fast-paced nature of YouTube Shorts. make the story as long as possible."""

# template = """You are a content writer for a big YouTuber. Given a topic, you will generate text for image generation and text for voice-over.

# **Instructions:**

# 1. **Generate text for image creation:** Extract key sentences from the provided topic that can be used to generate images. These sentences should be visually descriptive and capture the main ideas or scenes.
# 2. **Generate text for voice-over:** Extract key sentences from the provided topic and the image text that can be used for voice-over narration. These sentences should capture the main ideas or scenes, suitable for narration, and be crafted to grab viewers' attention.

# **Title:** [Title of the Short]  
# **Description:** [Brief description of the video]  
# **Tags:** [Relevant tags]  

# **Topic Text:**  
# {topic}  

# ---

# Note: The count of sentences for output depends on the topic.

# **Sentences for Image Generation:**  
# 1. [Visual description related to the hook]  
# 2. [Visual description related to Main Content Part 1]  
# 3. [Visual description related to Main Content Part 2]  
# .  
# .  
# n. [Visual description related to the call-to-action]  

# Note: The output should contain only the points. Make sure each sentence is concise and vivid, clearly depicting a scene or idea that can be visualized as an image. If any characters are present in the text, ensure all points describe characters with consistent characteristics such as age, gender, etc.

# ---

# Note: The count of sentences for output depends on the count of sentences in "text for image generation."

# **Sentences for Voice-Over:**  
# 1. [Voice-over line related to the hook]  
# 2. [Voice-over line related to Main Content Part 1]  
# 3. [Voice-over line related to Main Content Part 2]  
# .  
# .  
# n. [Voice-over line related to the call-to-action]  

# Note: The output should contain only the points. Make sure each sentence is concise, clear, and designed to capture the viewer's interest, effectively conveying the main points or scenes from the topic.
# """

# template = """
# You are a content writer for a prominent YouTuber. Given a specific topic, you will generate both text for image creation and text for voice-over narration.

# **Instructions:**

# 1. **Generate Text for Image Creation:** 
#    - Generate sentences from the provided topic that are visually descriptive and capture the main ideas or scenes. These sentences will guide the creation of compelling images.
#    - Ensure each sentence is concise, vivid, and clearly depicts a scene or idea that can be visualized as an image. If characters are involved, describe them consistently in terms of age, gender, etc.

# 2. **Generate Text for Voice-Over:** 
#    - Generate sentences from the provided topic and the image text that can be used for voice-over narration. These sentences should be engaging, suitable for narration.
#    - Ensure each sentence is concise, clear, and crafted to capture the viewer's interest, effectively conveying the main points or scenes from the topic.
#    - Make sure that each sentence is long enough to narrate for 10 seconds
   
# 3. **Ensure Synergy between Image and Voice-Over:**
#    - Ensure that each point in the image creation text corresponds logically and thematically with the corresponding point in the voice-over text, maintaining coherence throughout the video content.  
#    - The number of sentences for both should be same.
# Output format:

# **Title:** title  
# **Description:** description  
# **Tags:** tag1, tag2, tag3

# **Sentences for Image Generation:**
# 1. sentence-1
# 2. sentence-2
# 3. sentence-3
# and so on

# **Sentences for Voice-Over:**
# 1. sentence-1
# 2. sentence-2
# 3. sentence-3
# and so on

# **Topic Text:**  
# {topic}"""


#n. "If you enjoyed this video, don't forget to like, share, and subscribe for more content!"


# text_img_template = """Given the following YouTube Shorts script and topic, extract key sentences that can be used to generate images. The sentences should be visually descriptive and capture the main ideas or scenes from the script, suitable for a 50-60 seconds YouTube Short.

# **Script:**
# {script}

# **Topic:**
# {topic}

# **Sentences for Image Generation:**
# sentence 1
# sentence 2
# .
# .
# .
# sentence n

# Make sure each sentence is concise and vivid, clearly depicting a scene or idea that can be visualized as an image. If any characters are present in the text, ensure all points describe characters with consistent characteristics such as age, gender, etc. Include as many sentences as necessary to cover the main ideas or scenes from the script, keeping in mind the duration of 50-60 seconds."""


# text_speech_template = """Given the following YouTube Shorts script and topic, extract key sentences that can be used for a voice-over. The sentences should capture the main ideas or scenes from the script, suitable for narration, and be crafted to grab viewers' attention.

# **Script:**
# {script}

# **Topic:**
# {topic}

# **Sentences for Voice-Over:**
# sentence 1
# sentence 2
# .
# .
# .
# sentence n

# Make sure each sentence is concise, clear, and designed to capture the viewer's interest, effectively conveying the main points or scenes from the script. If any characters are present in the text, ensure all points describe characters with consistent characteristics such as age, gender, etc. Additionally, consider the tone needed to maintain engagement and interest throughout the video."""

# script_template = """Create a story for YouTube Shorts. The story should be engaging, concise (up to 60 seconds), and include a hook, main content, and a call-to-action (CTA). Use the information provided below to generate the script. Make sure to use a conversational and energetic tone suitable for a broad audience.

# **Title:** [Title of the Short]
# **Description:** [Brief description of the video]
# **Tags:** [Relevant tags]

# **Topic Text:**
# {topic}

# **Story:**

# **Hook:** An engaging introduction to capture viewers' attention.

# `main_content` - a big paragraph

# **Call-to-action:** Prompt viewers to like, comment, and subscribe.

# Make sure the script is punchy, direct, and visually descriptive to align with the fast-paced nature of YouTube Shorts."""

# script_template = """Create a script for YouTube Shorts. The script should be engaging, concise (up to 60 seconds), and include a hook, main content, and a call-to-action (CTA). Based on script generate text used for image generation and text used for voice-over. Use the information provided below to generate the script. Make sure to use a conversational and energetic tone suitable for a broad audience.

# **Title:** [Title of the Short]
# **Description:** [Brief description of the video]
# **Tags:** [Relevant tags]

# **Topic Text:**
# {topic}

# **Story:**

# **Hook:** An engaging introduction to capture viewers' attention.

# `main_content`

# **Call-to-action:** Prompt viewers to like, comment, and subscribe.

# **Sentences for Image Generation:**
# 1. [Visual description related to the hook]
# 2. [Visual description related to Main Content Part 1]
# 3. [Visual description related to Main Content Part 2]
# .
# .
# n. [Visual description related to the call-to-action]

# **Sentences for Voice-Over:**
# 1. [Voice-over line related to the hook]
# 2. [Voice-over line related to Main Content Part 1]
# 3. [Voice-over line related to Main Content Part 2]
# .
# .
# n. [Voice-over line related to the call-to-action]

# Make sure the script is punchy, direct, and visually descriptive to align with the fast-paced nature of YouTube Shorts."""


# text_img_template = """Given the following YouTube Shorts script and topic, extract key sentences that can be used to generate images. The sentences should be visually descriptive and capture the main ideas or scenes from the script, suitable for a 50-60 seconds YouTube Short.

# **Script:**
# {script}

# **Topic:**
# {topic}

# **Sentences for Image Generation:**
# 1. [Visual description related to the hook]
# 2. [Visual description related to Main Content Part 1]
# 3. [Visual description related to Main Content Part 2]
# .
# .
# n. [Visual description related to the call-to-action]

# Make sure each sentence is concise and vivid, clearly depicting a scene or idea that can be visualized as an image. If any characters are present in the text, ensure all points describe characters with consistent characteristics such as age, gender, etc. Include as many sentences as necessary to cover the main ideas or scenes from the script, keeping in mind the duration of 50-60 seconds."""

# text_img_template = """Given the following YouTube Shorts script and topic, extract key sentences that can be used to generate images. The sentences should be visually descriptive and capture the main ideas or scenes from the script.

# # **Script:**
# # {script}

# **Topic:**
# {topic}

# Note: count of sentences for output depends on topic
# **Sentences for Image Generation:**
# 1. [Visual description related to the hook]
# 2. [Visual description related to Main Content Part 1]
# 3. [Visual description related to Main Content Part 2]
# .
# .
# n. [Visual description related to the call-to-action]

# Note: The output should contain only the points 
# Make sure each sentence is concise and vivid, clearly depicting a scene or idea that can be visualized as an image. If any characters are preset in the text, ensure all points describe characters with consistent characteristics such as age, gender, etc."""


# text_speech_template = """Given the following YouTube Shorts script, text for image generation and topic, extract key sentences that can be used for a voice-over. The sentences should capture the main ideas or scenes from the script, suitable for narration, and be crafted to grab viewers' attention.

# **Script:**
# {script}

# **text for image generation**
# {text_img}

# **Topic:**
# {topic}

# Note: count of sentences for output depends on count of sentences in "text for image generation"
# **Sentences for Voice-Over:**
# 1. [Voice-over line related to the hook]
# 2. [Voice-over line related to Main Content Part 1]
# 3. [Voice-over line related to Main Content Part 2]
# .
# .
# n. [Voice-over line related to the call-to-action]

# Note: The output should contain only the points 
# Make sure each sentence is concise, clear, and designed to capture the viewer's interest, effectively conveying the main points or scenes from the script."""

# script_prompt = PromptTemplate.from_template(template)
# text_img_prompt = PromptTemplate.from_template(text_img_template)
# text_speech_prompt = PromptTemplate.from_template(text_speech_template)


# text_img_template = """Given the following YouTube Shorts script and topic, extract key sentences that can be used to generate images. The sentences should be visually descriptive and capture the main ideas or scenes from the script.

# **Script:**
# {script}

# **Topic:**
# {topic}

# **Sentences for Image Generation:**
# 1. [First descriptive sentence]
# 2. [Second descriptive sentence]
# 3. [Third descriptive sentence]
# 4. [Fourth descriptive sentence]
# 5. [Fifth descriptive sentence]

# Make sure each sentence is concise and vivid, clearly depicting a scene or idea that can be visualized as an image. If any characters are present in the text, ensure all points describe characters with consistent characteristics such as age, gender, etc."""


# template1 = """
# You are a content writer for a prominent YouTuber. Given a specific topic, you will generate both text for image creation and text for voice-over narration.

# **Instructions:**

# 1. **Generate Text for Image Creation:** 
#    - Generate sentences from the provided topic that are visually descriptive and capture the main ideas or scenes. These sentences will guide the creation of compelling images.
#    - Ensure each sentence is concise, vivid, and clearly depicts a scene or idea that can be visualized as an image. If characters are involved, describe them consistently in terms of age, gender, etc.

# 2. **Generate Text for Voice-Over:** 
#    - Generate sentences from the provided topic and the image text that can be used for voice-over narration. These sentences should be engaging, suitable for narration.
#    - Ensure each sentence is concise, clear, and crafted to capture the viewer's interest, effectively conveying the main points or scenes from the topic.
#    - Make sure that each sentence is long enough to narrate for 10 seconds
   
# 3. **Ensure Synergy between Image and Voice-Over:**
#    - Ensure that each point in the image creation text corresponds logically and thematically with the corresponding point in the voice-over text, maintaining coherence throughout the video content.

# **Topic:**  
# {topic}

# Output format:

# **Title:** title  
# **Description:** description  
# **Tags:** tag1, tag2, tag3

# **Sentences for Image Generation:**
# 1. sentence-1
# 2. sentence-2
# 3. sentence-3
# and so on

# **Sentences for Voice-Over:**
# 1. sentence-1
# 2. sentence-2
# 3. sentence-3
# and so on"""

# template2 = """You are an content writer working for a Youtuber. Given a topic and script, you will modify the script according to the instructions given below.

# **Instructions:**
# The script contains Title, Description, Tags, Sentences for Image Generation, Sentences for Voice-Over.
# - If count of sentences are not same in 'Sentences for Image Generation' and 'Sentences for Voice-Over', use your knowledge to make the count equalSSSSS
# - Ensure that each point in the 'Sentences for Image Generation' corresponds logically and thematically with the corresponding point in the 'Sentences for Voice-Over', maintaining coherence throughout the video content.
# - For 'Sentences for Image Generation' add a point in the beginning, that has Visual description related to the hook and a sentence at end saying thankyou.
# - For 'Sentences for Voice-Over' add a line related to the hook at the beginning that attracts audience attention and a line related to the Call-to-action - prompting viewers to like, comment, and subscribe at the end.
# - These sentences should be engaging, suitable for narration.

# **Topic:**  
# {topic}

# **Script:**  
# {script}

# return the output as dict enclosed in curly brackets"""

# prompt1 = PromptTemplate.from_template(template1)
# prompt2 = PromptTemplate.from_template(template2)

# Make sure that number of sentences in 'Sentences for Voice-Over' are one more than number of sentences in 'Sentences for Image Generation'. if not modify script.


# template1 = """Generate a YouTube Shorts script based on the following topic:

# Topic: {topic}

# The script should include:
# 1. **Title**: A catchy and engaging title.
# 2. **Description**: A brief description of the content.
# 3. **Tags**: Relevant tags for the video.
# 4. **Story**: A complete meaningful story that is engaging, clear, and crafted to capture the viewer's interest used for voice-over enclosed in "<story> story here <story>". Try to start with phrases like "Ever wondered", "Do you know", "What will happen if", "Have you considered", "Can you imagine", "Did you realize", "What if", "Have you thought about", "Do you ever think about", "Could it be that", "What do you think would happen if", "Are you aware that", "Did you ever notice", "How would it be if", "Can you believe".


# The script should be optimized for viewer engagement and SEO.

# **Example:**

# Topic: The benefits of meditation

# **Output:**

# Title: "Unlock the Power of Meditation in Just 60 Seconds!"

# Description: "Discover the incredible benefits of meditation in this quick and informative video. Learn how just a few minutes a day can transform your life!"

# Tags: meditation, mindfulness, mental health, wellness, stress relief, relaxation, daily habits, personal growth

# Story:
# <story>"Ever wondered how meditation can change your life? Meditation is a simple practice that can bring profound benefits. Just a few minutes a day can help reduce stress, improve concentration, and promote overall well-being. Whether you're new to meditation or a seasoned practitioner, incorporating this practice into your daily routine can lead to a healthier, happier life. Start your meditation journey today and experience the positive changes it can bring! If you enjoyed this video, hit the like button and subscribe for more wellness tips!<story>"""

# template1 = """Generate a YouTube Shorts script based on the following topic:

# Topic: {topic}

# The script should include:
# 1. **Title**: A catchy and engaging title.
# 2. **Description**: A brief description of the content.
# 3. **Tags**: Relevant tags for the video.
# 4. **Story**: A complete, meaningful story that is concise engaging, clear, and crafted to capture the viewer's interest. The story should be enclosed in "<story> story here <story>" and should be at least 150 words long. Start with phrases like "Do you know", "What will happen if", "Have you considered", "Can you imagine", "Did you realize", "Ever wondered", "What if", "Have you thought about", "Do you ever think about", "Could it be that", "What do you think would happen if", "Are you aware that", "Did you ever notice", "How would it be if", "Can you believe".

# The script should be optimized for viewer engagement and SEO.

# **Example:**

# Topic: The benefits of meditation

# **Output:**

# Title: "Unlock the Power of Meditation in Just 60 Seconds!"

# Description: "Discover the incredible benefits of meditation in this quick and informative video. Learn how just a few minutes a day can transform your life!"

# Tags: meditation, mindfulness, mental health, wellness, stress relief, relaxation, daily habits, personal growth

# Story:
# <story>"Ever wondered how meditation can change your life? Meditation is a simple practice that can bring profound benefits. Just a few minutes a day can help reduce stress, improve concentration, and promote overall well-being. Imagine starting your day with a calm and focused mind, ready to tackle any challenge. Whether you're new to meditation or a seasoned practitioner, incorporating this practice into your daily routine can lead to a healthier, happier life. Picture yourself finding peace in moments of chaos, and clarity in times of confusion. Start your meditation journey today and experience the positive changes it can bring! If you enjoyed this video, hit the like button and subscribe for more wellness tips!<story>"
# """

# template1 = """Generate a YouTube Shorts script based on the following topic:

# Topic: {topic}

# The script should include:
# 1. **Title**: A catchy and engaging title.
# 2. **Description**: A brief description of the content.
# 3. **Tags**: Relevant tags for the video.
# 4. **Story**: A complete, meaningful story that is concise, engaging, clear, and crafted to capture the viewer's interest. The story should be enclosed in "<story> story here <story>" and should be 7 sentences long. Start with phrases like "Did you know", "Imagine if", "Ever wondered how", "Have you seen", "What if you could", "Do you believe", "Could it be true that", "How does it feel to", "Are you ready to".

# The script should be optimized for viewer engagement and SEO.

# **Example:**

# Topic: The Power of India

# **Output:**

# Title: "Unveiling the Majesty of India: A Journey Through Its Rich Heritage!"

# Description: "Embark on a captivating journey through the vibrant tapestry of India's culture, history, and resilience. Discover what makes India truly incredible!"

# Tags: India, Indian culture, heritage, history, diversity, travel, spirituality, tradition

# Story:
# <story>"Did you know India is a treasure trove of culture and diversity? Imagine if you could witness the timeless traditions of Diwali illuminating the night sky, or the majestic architecture of the Taj Mahal standing as a testament to eternal love. Ever wondered how a country so vast could harmonize myriad languages, cuisines, and customs? Have you seen the breathtaking landscapes from the snowy peaks of the Himalayas to the sun-kissed beaches of Goa? India's allure lies not just in its landmarks, but in the resilience of its people and their unwavering spirit. Could it be true that every corner of India tells a story of ancient wisdom and modern innovation? Are you ready to immerse yourself in the magic of India and experience its timeless charm? Join us on this journey through India's rich heritage and discover why it continues to captivate hearts around the world. If you're enchanted by India's beauty, hit the like button and subscribe for more cultural explorations!<story>"
# """

# template1 = """Generate a YouTube Shorts script based on the following topic:

# Topic: {topic}

# The script should include:
# 1. **Title**: A catchy and engaging title.
# 2. **Description**: A brief description of the content.
# 3. **Tags**: Relevant tags for the video.
# 4. **Story**: A complete, meaningful story that is concise, engaging, clear, and crafted to capture the viewer's interest. The story should be enclosed in "<story> story here <story>" and should be 7 sentences long. Start with phrases like "Did you know", "Imagine if", "Ever wondered how", "Have you seen", "What if you could", "Do you believe", "Could it be true that", "How amazing would it be if", "Are you ready to".

# The script should be optimized for viewer engagement and SEO.

# **Example:**

# Topic: Exploring Ancient Egypt

# **Output:**

# Title: "Unlocking the Mysteries of Ancient Egypt: A Journey through Time!"

# Description: "Embark on an adventure through the wonders of ancient Egypt. Discover the secrets of the pyramids, pharaohs, and more!"

# Tags: Ancient Egypt, history, archaeology, pyramids, pharaohs, ancient civilizations, Egyptology, travel

# Story:
# <story>"Did you know ancient Egypt is filled with mysteries waiting to be uncovered? Imagine if you could walk among the towering pyramids that have stood for thousands of years, marveling at their architectural brilliance. Ever wondered how the mighty pharaohs ruled over this ancient land, their legacy etched in hieroglyphs and artifacts? Have you seen the breathtaking artifacts that tell stories of gods, rituals, and daily life in this ancient civilization? Egypt's allure isn't just in its monuments; it's in the timeless tales of innovation and mythology woven into its history. Could it be true that every artifact holds a piece of a puzzle, revealing more about ancient Egyptian life? How amazing would it be if you could experience the grandeur of Karnak or the serenity of the Nile firsthand? Join us on a journey through ancient Egypt's rich heritage and uncover the wonders that continue to captivate the world. If you're fascinated by history and adventure, hit the like button and subscribe for more explorations into ancient civilizations!<story>"
# """

template1 = """Generate a YouTube Shorts script based on the following topic:

Topic: {topic}

The script should include:
1. **Title**: A catchy and engaging title.
2. **Description**: A brief description of the content.
3. **Tags**: Relevant tags for the video.
4. **Story**: A complete, meaningful story that is concise, engaging, clear, and crafted to capture the viewer's interest. The story should be enclosed in "<story> story here <story>" and should be 7 sentences long. Start with phrases like "Did you know", "Imagine if", "Ever wondered how", "Have you seen", "What if you could", "Do you believe", "Could it be true that", "How amazing would it be if", "Are you ready to".

The script should be optimized for viewer engagement and SEO.

**Example:**

Topic: The Secrets of Ancient Civilizations

**Output:**

Title: "Unlocking the Secrets of Ancient Civilizations: Lost Worlds Revealed!"

Description: "Journey through time to uncover the secrets of ancient civilizations and their lasting impact on our world."

Tags: Ancient civilizations, history, archaeology, lost worlds, exploration, culture, heritage

Story:
<story>"Ever wondered how ancient civilizations shaped our world? Imagine if you could walk through the ruins of lost cities and uncover their secrets. Did you know the Maya had advanced knowledge of astronomy? The Romans built incredible structures that still stand today. Each civilization left a legacy of innovation and culture. How amazing would it be to explore these ancient worlds? Hit like and subscribe for more historical adventures!<story>"
"""

template2 = """Generate text used for image generation based on the following script:

Script:
{script}

For each sentence in the story, provide a detailed description of the image that should be generated along with sentence enclosed in <sentence>. The descriptions should capture the essence and context of each sentence. Each output sentence is enclosed in <image> sentence here <image>. 

**Example:**

Script:
"Meditation is a simple practice that can bring profound benefits. Just a few minutes a day can help reduce stress, improve concentration, and promote overall well-being. Whether you're new to meditation or a seasoned practitioner, incorporating this practice into your daily routine can lead to a healthier, happier life. Start your meditation journey today and experience the positive changes it can bring!"

**Output format:**

<sentence>Meditation is a simple practice that can bring profound benefits."<sentence>
<image>An individual sitting cross-legged on a serene beach at sunrise, with a calm expression, symbolizing the simplicity and profound impact of meditation.<image>

<sentence>Just a few minutes a day can help reduce stress, improve concentration, and promote overall well-being.<sentence>
<image>A close-up of a clock showing a few minutes past the hour, with a background of a person meditating peacefully, representing the short time required for meditation's benefits.<image>

<sentence>Whether you're new to meditation or a seasoned practitioner, incorporating this practice into your daily routine can lead to a healthier, happier life.<sentence>
<image>A split image showing a beginner following a guided meditation on a phone and an experienced practitioner meditating in nature, illustrating the inclusivity and benefits of meditation for all levels.<image>

<sentence>Start your meditation journey today and experience the positive changes it can bring!<sentence>
<image>A person starting their day with a smile, meditating in a tranquil garden, symbolizing the beginning of a transformative journey through meditation.<image>
"""

# template2 = """Generate text used for image generation based on the following script:

# Script:
# {script}

# For each sentence in the story, provide a detailed description of the image that should be generated. The descriptions should capture the essence and context of each sentence. each output sentence is enclosed in <image> sentence here <image>

# **Example:**

# Script:
# "Meditation is a simple practice that can bring profound benefits. Just a few minutes a day can help reduce stress, improve concentration, and promote overall well-being. Whether you're new to meditation or a seasoned practitioner, incorporating this practice into your daily routine can lead to a healthier, happier life. Start your meditation journey today and experience the positive changes it can bring!"

# **Output:**

# <image>An individual sitting cross-legged on a serene beach at sunrise, with a calm expression, symbolizing the simplicity and profound impact of meditation.<image>
# <image>A close-up of a clock showing a few minutes past the hour, with a background of a person meditating peacefully, representing the short time required for meditation's benefits.<image>
# <image>A split image showing a beginner following a guided meditation on a phone and an experienced practitioner meditating in nature, illustrating the inclusivity and benefits of meditation for all levels.<image>
# <image>A person starting their day with a smile, meditating in a tranquil garden, symbolizing the beginning of a transformative journey through meditation.<image>
# """

prompt1 = PromptTemplate(template=template1, input_variables=["topic"])
prompt2 = PromptTemplate(template=template2, input_variables=["script"])