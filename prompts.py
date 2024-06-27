from langchain.prompts import PromptTemplate

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


prompt1 = PromptTemplate(template=template1, input_variables=["topic"])
prompt2 = PromptTemplate(template=template2, input_variables=["script"])