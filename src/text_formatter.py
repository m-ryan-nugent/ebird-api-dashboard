import openai


class TextFormatter:
    def __init__(self, openai_api_key):
        self.client = openai.OpenAI(api_key=openai_api_key)

    def get_species_descriptions(self, species_list):
        descriptions = {}
        for species in species_list:
            prompt = (
                "Provide a one-sentence description of the bird species"
                f" '{species}'."
            )

            try:
                completion = self.client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                    n=1,
                    stop=None,
                    temperature=0.1,
                )
                description = completion.choices[0].message.content
                descriptions[species] = description

            except openai.OpenAIError as e:
                descriptions[species] = f"Error retrieving description: {e}"

        return descriptions
