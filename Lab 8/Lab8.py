class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid  # Keep as string
        self.title = title
        self.year = int(year)

    def __str__(self):
        return f"UID: {self.uid}\nTitle: {self.title}\nYear: {self.year}"

    def __eq__(self, other):
        return self.uid == other.uid

    def is_recent(self, n):
        return self.year >= 2025 - n


class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = int(pages)

    def __str__(self):
        return (f"UID: {self.uid}\nTitle: {self.title}\nYear: {self.year}"
                f"\nAuthor: {self.author}\nPages: {self.pages}")


class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return (f"UID: {self.uid}\nTitle: {self.title}\nYear: {self.year}"
                f"\nJournal: {self.journal}\nDOI: {self.doi}")


class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration_minutes):
        super().__init__(uid, title, year)
        self.host = host
        self.duration_minutes = int(duration_minutes)

    def __str__(self):
        return (f"UID: {self.uid}\nTitle: {self.title}\nYear: {self.year}"
                f"\nHost: {self.host}\nDuration: {self.duration_minutes} minutes")


def save_to_file(items, filename):
    try:
        with open(filename, "w") as file:
            for item in items:
                if isinstance(item, Book):
                    file.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
                elif isinstance(item, Article):
                    file.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
                elif isinstance(item, Podcast):
                    file.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration_minutes}\n")
    except Exception as e:
        print("Error while saving:", e)


def load_from_file(filename):
    items = []
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] == "Book":
                    items.append(Book(parts[1], parts[2], parts[3], parts[4], parts[5]))
                elif parts[0] == "Article":
                    items.append(Article(parts[1], parts[2], parts[3], parts[4], parts[5]))
                elif parts[0] == "Podcast":
                    items.append(Podcast(parts[1], parts[2], parts[3], parts[4], parts[5]))
    except Exception as e:
        print("Error while loading:", e)
    return items


archive_items = [
    Book("B001", "Brainrot Terminology", 2018, "Tralalero Tralala", 775),
    Book("B002", "A History On Brainrot", 2020, "Bombardino Crocodilo", 464),
    Article("A101", "How The Prius C is Killing Brr Brr Patapim", 2022, "Nature", "10.1234/qc567"),
    Article("A102", "How 10 Hours of Scrolling Instagram Reels Every Day Improves Your Life", 2019, "Science", "10.5678/ai999"),
    Podcast("P301", "The Lion Does Not Concern Himself With Python \"Developers\"", 2023, "Terry Davis", 6942031),
    Podcast("P302", "How Redeem Google Play Gift Cards", 2021, "Arjun Singh", 30)
]

save_to_file(archive_items, "archive.txt")
loaded_items = load_from_file("archive.txt")

print("All Items:")
for item in loaded_items:
    if isinstance(item, Book):
        print("Book:")
    elif isinstance(item, Article):
        print("Article:")
    elif isinstance(item, Podcast):
        print("Podcast:")
    print(item)
    print("\n")

print("\n")
print("-------------------------------------------")
print("\n")

print("\nRecent Items:")
for item in loaded_items:
    if item.is_recent(5):
        if isinstance(item, Book):
            print("Book:")
        elif isinstance(item, Article):
            print("Article:")
        elif isinstance(item, Podcast):
            print("Podcast:")
        print(item)
        print("\n")

print("\n")
print("-------------------------------------------")
print("\n")

print("\nArticles with DOI starting '10.1234':")
for item in loaded_items:
    if isinstance(item, Article) and item.doi.startswith("10.1234"):
        print(item)
        print("\n")
