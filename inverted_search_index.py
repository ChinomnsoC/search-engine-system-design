class InvertedIndexSearch:
    def __init__(self, studies):
        """
        Initialize the search engine with a list of studies.
        Each study is a dictionary with 'study_id', 'title', and 'description'.
        """
        self.studies = studies
        self.inverted_index = self.build_inverted_index()
        print("\n🔍 Built Inverted Index:", self.inverted_index)  # Debugging

    def build_inverted_index(self):
        """
        Build an inverted index mapping keywords to a list of study titles.
        """
        inverted_index = {}
        
        for study in self.studies:
            words = set((study["title"] + " " + study["description"]).lower().split())  # Tokenizing words
            for word in words:
                if word not in inverted_index:
                    inverted_index[word] = []
                inverted_index[word].append(study["title"])
        
        return inverted_index

    def search_studies(self, keyword):
        """
        Return a list of study titles that contain the given keyword.
        """
        keyword = keyword.lower()
        print(f"\n🔍 Searching for: {keyword}")  # Debugging
        
        if keyword in self.inverted_index:
            results = self.inverted_index[keyword]
            print(f"Found {len(results)} results: {results}")  # Debugging
            return results
        else:
            print("No results found.")
            return []
        

# Sample dataset (research studies)
studies = [
    {"study_id": 1, "title": "Machine Learning in Psychology", "description": "Understanding cognition using ML"},
    {"study_id": 2, "title": "Behavioral Neuroscience", "description": "Study on human behavior and learning"},
    {"study_id": 3, "title": "AI and Cognitive Science", "description": "Exploring cognition and perception with AI"},
]

# Initialize search engine
search_engine = InvertedIndexSearch(studies)

# Test search
search_engine.search_studies("cognition")
search_engine.search_studies("machine")
search_engine.search_studies("AI")
search_engine.search_studies("biology")  # Should return no results
