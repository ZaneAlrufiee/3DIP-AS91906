questions_by_subject = {
    "Math": [
        # Easy Questions
        ("What is 2 + 2?", ["2", "3", "4", "5"], "c", "easy"),
        ("What is 5 - 3?", ["1", "2", "3", "4"], "b", "easy"),
        ("What is 3 * 3?", ["6", "7", "8", "9"], "d", "easy"),
        ("What is 10 / 2?", ["3", "5", "6", "7"], "b", "easy"),
        ("What is 7 + 6?", ["10", "11", "12", "13"], "d", "easy"),
        ("What is 9 - 5?", ["2", "3", "4", "5"], "c", "easy"),
        ("What is 8 * 1?", ["7", "8", "9", "10"], "b", "easy"),
        ("What is 12 - 8?", ["3", "4", "5", "6"], "b", "easy"),
        ("What is 14 / 2?", ["5", "6", "7", "8"], "c", "easy"),
        ("What is 11 + 9?", ["18", "19", "20", "21"], "c", "easy"),
        # Medium Questions
        ("What is 15 / 3?", ["3", "4", "5", "6"], "c", "medium"),
        ("What is 12 + 8?", ["18", "20", "21", "22"], "b", "medium"),
        ("What is the square root of 64?", ["6", "7", "8", "9"], "c", "medium"),
        ("What is 45 + 15?", ["55", "60", "65", "70"], "b", "medium"),
        ("What is 81 - 19?", ["59", "60", "61", "62"], "c", "medium"),
        ("What is 9 * 7?", ["62", "63", "64", "65"], "b", "medium"),
        ("What is 144 / 12?", ["10", "11", "12", "13"], "c", "medium"),
        ("What is 50% of 200?", ["75", "90", "100", "110"], "c", "medium"),
        ("What is 3^3?", ["9", "27", "30", "81"], "b", "medium"),
        ("What is 5 factorial (5!)?", ["60", "100", "120", "150"], "c", "medium"),
        # Hard Questions
        ("What is 25 * 25?", ["525", "625", "725", "825"], "b", "hard"),
        ("What is the value of π (pi) to 2 decimal places?", ["3.12", "3.14", "3.16", "3.18"], "b", "hard"),
        ("What is the derivative of x^2?", ["x", "2x", "x^3", "2x^2"], "b", "hard"),
        ("What is the integral of 2x?", ["x^2 + C", "2x^2 + C", "2x + C", "4x + C"], "a", "hard"),
        ("What is the limit of (1 + 1/n)^n as n approaches infinity?", ["1", "2", "e", "∞"], "c", "hard"),
        ("What is the sum of the first 100 natural numbers?", ["5000", "5050", "5100", "5150"], "b", "hard"),
        ("What is the determinant of a 2x2 matrix [[a, b], [c, d]]?", ["ad - bc", "ab + cd", "ad + bc", "ab - cd"], "a", "hard"),
        ("What is Euler's number (e) to 2 decimal places?", ["2.71", "2.72", "2.73", "2.74"], "a", "hard"),
        ("What is the Pythagorean theorem?", ["a^2 + b^2 = c^2", "a^2 - b^2 = c^2", "a^3 + b^3 = c^3", "a + b = c"], "a", "hard"),
        ("What is the standard form of a quadratic equation?", ["ax^2 + bx + c = 0", "ax + b = 0", "ax^3 + bx^2 + c = 0", "ax^4 + bx^3 + c = 0"], "a", "hard")
    ],
    "Science": [
        # Easy Questions
        ("What planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "b", "easy"),
        ("What is the boiling point of water?", ["90°C", "95°C", "100°C", "105°C"], "c", "easy"),
        ("What gas do plants absorb from the atmosphere?", ["Oxygen", "Hydrogen", "Carbon Dioxide", "Nitrogen"], "c", "easy"),
        ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "N2"], "a", "easy"),
        ("What force keeps us on the ground?", ["Magnetism", "Gravity", "Friction", "Inertia"], "b", "easy"),
        ("What organ pumps blood through the body?", ["Lungs", "Brain", "Heart", "Liver"], "c", "easy"),
        ("Which planet is closest to the Sun?", ["Earth", "Venus", "Mars", "Mercury"], "d", "easy"),
        ("What is the hardest natural substance on Earth?", ["Gold", "Iron", "Diamond", "Quartz"], "c", "easy"),
        ("Which gas is most abundant in Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"], "b", "easy"),
        ("What is the main gas found in the air we breathe?", ["Oxygen", "Nitrogen", "Carbon Dioxide", "Helium"], "b", "easy"),
        # Medium Questions
        ("What is the chemical symbol for gold?", ["Au", "Ag", "Pb", "Pt"], "a", "medium"),
        ("What is the process by which plants make food?", ["Photosynthesis", "Respiration", "Digestion", "Circulation"], "a", "medium"),
        ("Which part of the cell contains genetic material?", ["Nucleus", "Cytoplasm", "Mitochondria", "Ribosomes"], "a", "medium"),
        ("What type of bond shares electrons?", ["Ionic", "Covalent", "Hydrogen", "Metallic"], "b", "medium"),
        ("What is the basic unit of life?", ["Atom", "Molecule", "Cell", "Organ"], "c", "medium"),
        ("What are the building blocks of proteins?", ["Carbohydrates", "Nucleotides", "Lipids", "Amino Acids"], "d", "medium"),
        ("What element is most abundant in the human body?", ["Oxygen", "Carbon", "Hydrogen", "Nitrogen"], "a", "medium"),
        ("Which blood type is known as the universal donor?", ["A", "B", "AB", "O"], "d", "medium"),
        ("What is the powerhouse of the cell?", ["Nucleus", "Mitochondria", "Ribosomes", "Golgi Apparatus"], "b", "medium"),
        ("Which planet has the most moons?", ["Mars", "Jupiter", "Saturn", "Uranus"], "b", "medium"),
        # Hard Questions
        ("What is the most abundant gas in Earth's atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], "c", "hard"),
        ("What is the speed of light in a vacuum?", ["300,000 km/s", "150,000 km/s", "100,000 km/s", "200,000 km/s"], "a", "hard"),
        ("Who developed the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "b", "hard"),
        ("What is the atomic number of carbon?", ["6", "8", "12", "14"], "a", "hard"),
        ("What is the most abundant element in the universe?", ["Oxygen", "Hydrogen", "Helium", "Carbon"], "b", "hard"),
        ("What is the rarest naturally occurring element on Earth?", ["Francium", "Uranium", "Plutonium", "Radium"], "a", "hard"),
        ("Which scientist is known for the laws of motion?", ["Galileo Galilei", "Albert Einstein", "Isaac Newton", "Marie Curie"], "c", "hard"),
        ("What is the primary component of the Sun?", ["Oxygen", "Helium", "Hydrogen", "Carbon"], "c", "hard"),
        ("Which element has the highest melting point?", ["Tungsten", "Iron", "Gold", "Platinum"], "a", "hard"),
        ("What is the smallest unit of matter?", ["Atom", "Molecule", "Proton", "Electron"], "a", "hard")
    ],
    "History": [
        # Easy Questions
        ("Who was the first President of the United States?", ["Abraham Lincoln", "George Washington", "Thomas Jefferson", "John Adams"], "b", "easy"),
        ("In what year did the Titanic sink?", ["1912", "1914", "1920", "1908"], "a", "easy"),
        ("What empire was ruled by Julius Caesar?", ["Roman", "Greek", "Egyptian", "Persian"], "a", "easy"),
        ("Who discovered America?", ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "James Cook"], "a", "easy"),
        ("Who was the first man to step on the moon?", ["Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "John Glenn"], "a", "easy"),
        ("Which ancient civilization built the pyramids?", ["Aztec", "Mayan", "Roman", "Egyptian"], "d", "easy"),
        ("Who was the first female Prime Minister of the UK?", ["Theresa May", "Margaret Thatcher", "Angela Merkel", "Indira Gandhi"], "b", "easy"),
        ("Which war ended with the Treaty of Versailles?", ["World War I", "World War II", "The Civil War", "The Revolutionary War"], "a", "easy"),
        ("Who wrote the Declaration of Independence?", ["George Washington", "Thomas Jefferson", "Benjamin Franklin", "John Adams"], "b", "easy"),
        ("Which country gifted the Statue of Liberty to the USA?", ["Germany", "France", "Spain", "Italy"], "b", "easy"),
        # Medium Questions
        ("Which war was fought between the North and South regions in the United States?", ["World War I", "World War II", "The Civil War", "The Revolutionary War"], "c", "medium"),
        ("Which country was Adolf Hitler born in?", ["Germany", "Austria", "Poland", "Hungary"], "b", "medium"),
        ("Who was the British Prime Minister during World War II?", ["Neville Chamberlain", "Winston Churchill", "Clement Attlee", "Margaret Thatcher"], "b", "medium"),
        ("Which event began on July 28, 1914?", ["The Great Depression", "World War I", "World War II", "The Cold War"], "b", "medium"),
        ("What was the main cause of the American Civil War?", ["Taxation", "Territory", "Slavery", "Religion"], "c", "medium"),
        ("Who was the leader of the Soviet Union during World War II?", ["Vladimir Lenin", "Joseph Stalin", "Nikita Khrushchev", "Leonid Brezhnev"], "b", "medium"),
        ("What was the original name of New York City?", ["New Amsterdam", "New Paris", "New London", "New Madrid"], "a", "medium"),
        ("Which ancient civilization built Machu Picchu?", ["Aztec", "Inca", "Mayan", "Olmec"], "b", "medium"),
        ("Who was the first emperor of China?", ["Qin Shi Huang", "Han Wudi", "Liu Bang", "Kublai Khan"], "a", "medium"),
        ("Which war was the Battle of Gettysburg a part of?", ["World War I", "World War II", "The Civil War", "The Revolutionary War"], "c", "medium"),
        # Hard Questions
        ("Which treaty ended World War I?", ["Treaty of Paris", "Treaty of Versailles", "Treaty of Tordesillas", "Treaty of Ghent"], "b", "hard"),
        ("What was the name of the ship on which the Pilgrims traveled to America?", ["Mayflower", "Santa Maria", "Beagle", "Endeavour"], "a", "hard"),
        ("Who was the longest reigning British monarch before Queen Elizabeth II?", ["Queen Victoria", "King George III", "Queen Mary I", "Queen Elizabeth I"], "a", "hard"),
        ("Which explorer was the first to circumnavigate the globe?", ["Christopher Columbus", "Vasco da Gama", "Ferdinand Magellan", "John Cabot"], "c", "hard"),
        ("Which Roman Emperor was the first to convert to Christianity?", ["Julius Caesar", "Augustus", "Constantine", "Nero"], "c", "hard"),
        ("What event started on October 29, 1929?", ["World War I", "World War II", "The Great Depression", "The Cold War"], "c", "hard"),
        ("Who was the first person to reach the South Pole?", ["Roald Amundsen", "Robert Falcon Scott", "Ernest Shackleton", "James Clark Ross"], "a", "hard"),
        ("Which empire was ruled by Genghis Khan?", ["Ottoman", "Mongol", "Roman", "Ming"], "b", "hard"),
        ("What year did the Berlin Wall fall?", ["1987", "1988", "1989", "1990"], "c", "hard"),
        ("Which battle is considered the turning point of World War II in the Pacific?", ["Battle of the Coral Sea", "Battle of Iwo Jima", "Battle of Midway", "Battle of Okinawa"], "c", "hard")
    ],
    "Geography": [
        # Easy Questions
        ("What is the largest continent?", ["Africa", "Asia", "Europe", "Antarctica"], "b", "easy"),
        ("Which is the longest river in the world?", ["Amazon", "Nile", "Yangtze", "Mississippi"], "b", "easy"),
        ("Which ocean is the largest?", ["Atlantic", "Indian", "Arctic", "Pacific"], "d", "easy"),
        ("What is the capital of France?", ["Berlin", "London", "Paris", "Rome"], "c", "easy"),
        ("Which country is known as the Land of the Rising Sun?", ["China", "South Korea", "Japan", "Thailand"], "c", "easy"),
        ("Which country has the most population?", ["India", "China", "USA", "Indonesia"], "b", "easy"),
        ("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Brisbane"], "c", "easy"),
        ("Which desert is the largest in the world?", ["Gobi", "Sahara", "Arctic", "Antarctic"], "d", "easy"),
        ("What is the official language of Brazil?", ["Spanish", "English", "Portuguese", "French"], "c", "easy"),
        ("Which country is famous for tulips and windmills?", ["Germany", "Belgium", "Netherlands", "Denmark"], "c", "easy"),
        # Medium Questions
        ("Which country is the largest by land area?", ["China", "Canada", "Russia", "USA"], "c", "medium"),
        ("Which mountain range separates Europe and Asia?", ["Himalayas", "Andes", "Rockies", "Ural"], "d", "medium"),
        ("What is the smallest continent?", ["Europe", "Australia", "South America", "Antarctica"], "b", "medium"),
        ("Which river flows through the Grand Canyon?", ["Missouri", "Colorado", "Mississippi", "Rio Grande"], "b", "medium"),
        ("Which country is both in Asia and Europe?", ["Turkey", "Russia", "Kazakhstan", "Georgia"], "b", "medium"),
        ("What is the largest island in the world?", ["Greenland", "Borneo", "Madagascar", "New Guinea"], "a", "medium"),
        ("Which ocean surrounds the Maldives?", ["Pacific", "Atlantic", "Indian", "Arctic"], "c", "medium"),
        ("What is the capital of Canada?", ["Toronto", "Ottawa", "Vancouver", "Montreal"], "b", "medium"),
        ("Which country is known as the Pearl of the Indian Ocean?", ["Maldives", "Sri Lanka", "Mauritius", "Seychelles"], "b", "medium"),
        ("Which river is the longest in Asia?", ["Yellow", "Yangtze", "Mekong", "Ganges"], "b", "medium"),
        # Hard Questions
        ("Which is the smallest country in the world by land area?", ["Monaco", "Nauru", "Vatican City", "San Marino"], "c", "hard"),
        ("Which mountain is the highest in North America?", ["Denali", "Mount Logan", "Mount Whitney", "Mount Elbert"], "a", "hard"),
        ("Which African country was never colonized?", ["Ethiopia", "Nigeria", "Ghana", "Kenya"], "a", "hard"),
        ("What is the most populous city in the world?", ["New York", "Shanghai", "Tokyo", "Mumbai"], "c", "hard"),
        ("Which desert is the coldest?", ["Gobi", "Kalahari", "Sahara", "Antarctic"], "d", "hard"),
        ("Which sea is the saltiest?", ["Red Sea", "Dead Sea", "Caspian Sea", "Mediterranean Sea"], "b", "hard"),
        ("Which European country has the most lakes?", ["Finland", "Sweden", "Norway", "Switzerland"], "a", "hard"),
        ("Which country has the most time zones?", ["Russia", "USA", "China", "France"], "d", "hard"),
        ("Which island country lies between Greenland and Norway?", ["Iceland", "Faroe Islands", "Svalbard", "Shetland Islands"], "a", "hard"),
        ("Which river is known as the 'River of Sorrows'?", ["Yellow River", "Yangtze River", "Ganges River", "Mekong River"], "a", "hard")
    ],
    "Literature": [
        # Easy Questions
        ("Who wrote 'Romeo and Juliet'?", ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"], "b", "easy"),
        ("Which book begins with 'Call me Ishmael'?", ["Moby Dick", "To Kill a Mockingbird", "The Great Gatsby", "1984"], "a", "easy"),
        ("Who wrote 'The Hobbit'?", ["J.R.R. Tolkien", "C.S. Lewis", "J.K. Rowling", "George R.R. Martin"], "a", "easy"),
        ("Who wrote 'Pride and Prejudice'?", ["Jane Austen", "Emily Brontë", "Mary Shelley", "Charlotte Brontë"], "a", "easy"),
        ("Who is the author of 'The Catcher in the Rye'?", ["Ernest Hemingway", "J.D. Salinger", "F. Scott Fitzgerald", "George Orwell"], "b", "easy"),
        ("Which novel features the character Atticus Finch?", ["1984", "To Kill a Mockingbird", "The Catcher in the Rye", "Brave New World"], "b", "easy"),
        ("Who wrote 'Harry Potter'?", ["J.R.R. Tolkien", "J.K. Rowling", "Rick Riordan", "C.S. Lewis"], "b", "easy"),
        ("Who wrote 'A Christmas Carol'?", ["Charles Dickens", "Mark Twain", "William Shakespeare", "George Eliot"], "a", "easy"),
        ("Which book is set on a deserted island?", ["The Hobbit", "Lord of the Flies", "Robinson Crusoe", "Gulliver's Travels"], "b", "easy"),
        ("Who wrote 'The Great Gatsby'?", ["Ernest Hemingway", "J.D. Salinger", "F. Scott Fitzgerald", "George Orwell"], "c", "easy"),
        # Medium Questions
        ("Who is the author of 'Pride and Prejudice'?", ["Emily Brontë", "Jane Austen", "Mary Shelley", "Charlotte Brontë"], "b", "medium"),
        ("Who wrote 'Crime and Punishment'?", ["Fyodor Dostoevsky", "Leo Tolstoy", "Anton Chekhov", "Vladimir Nabokov"], "a", "medium"),
        ("Who created the character Sherlock Holmes?", ["Arthur Conan Doyle", "Agatha Christie", "Ian Fleming", "Raymond Chandler"], "a", "medium"),
        ("What is the pen name of Samuel Langhorne Clemens?", ["Lewis Carroll", "George Orwell", "Mark Twain", "H.G. Wells"], "c", "medium"),
        ("Who wrote '1984'?", ["George Orwell", "Aldous Huxley", "Ray Bradbury", "H.G. Wells"], "a", "medium"),
        ("Which novel is set in the fictional town of Maycomb?", ["Moby Dick", "To Kill a Mockingbird", "The Great Gatsby", "1984"], "b", "medium"),
        ("Who wrote 'One Hundred Years of Solitude'?", ["Gabriel García Márquez", "Isabel Allende", "Jorge Luis Borges", "Mario Vargas Llosa"], "a", "medium"),
        ("Which author created the character 'Hercule Poirot'?", ["Arthur Conan Doyle", "Agatha Christie", "Dorothy L. Sayers", "Rex Stout"], "b", "medium"),
        ("Who wrote 'Frankenstein'?", ["Mary Shelley", "Bram Stoker", "Robert Louis Stevenson", "H.G. Wells"], "a", "medium"),
        ("Who wrote 'The Odyssey'?", ["Homer", "Virgil", "Sophocles", "Aristotle"], "a", "medium"),
        # Hard Questions
        ("In which novel is the character Captain Ahab featured?", ["War and Peace", "Les Misérables", "Moby Dick", "The Odyssey"], "c", "hard"),
        ("Who wrote 'The Brothers Karamazov'?", ["Leo Tolstoy", "Fyodor Dostoevsky", "Anton Chekhov", "Ivan Turgenev"], "b", "hard"),
        ("Who wrote 'Les Misérables'?", ["Victor Hugo", "Gustave Flaubert", "Alexandre Dumas", "Honoré de Balzac"], "a", "hard"),
        ("Which playwright wrote 'Waiting for Godot'?", ["Samuel Beckett", "Tennessee Williams", "Arthur Miller", "Harold Pinter"], "a", "hard"),
        ("Who wrote 'Ulysses'?", ["James Joyce", "William Faulkner", "Virginia Woolf", "Marcel Proust"], "a", "hard"),
        ("Which author wrote 'Brave New World'?", ["Aldous Huxley", "George Orwell", "Ray Bradbury", "Philip K. Dick"], "a", "hard"),
        ("Which 19th-century novel features the character Heathcliff?", ["Pride and Prejudice", "Wuthering Heights", "Jane Eyre", "Great Expectations"], "b", "hard"),
        ("Who wrote 'A Tale of Two Cities'?", ["Charles Dickens", "Thomas Hardy", "George Eliot", "Mark Twain"], "a", "hard"),
        ("Which novel begins with the line 'It was the best of times, it was the worst of times'?", ["Moby Dick", "Pride and Prejudice", "A Tale of Two Cities", "Great Expectations"], "c", "hard"),
        ("Who wrote 'The Divine Comedy'?", ["Dante Alighieri", "Geoffrey Chaucer", "John Milton", "William Blake"], "a", "hard")
    ],
    "Technology": [
        # Easy Questions
        ("Who founded Microsoft?", ["Steve Jobs", "Bill Gates", "Elon Musk", "Larry Page"], "b", "easy"),
        ("What does 'HTTP' stand for?", ["HyperText Transfer Protocol", "High-Tech Transfer Protocol", "HyperText Transfer Program", "High-Tech Transfer Program"], "a", "easy"),
        ("Which social media platform is known for tweets?", ["Facebook", "Instagram", "Twitter", "LinkedIn"], "c", "easy"),
        ("What is the name of Apple's mobile operating system?", ["Android", "iOS", "Windows", "Linux"], "b", "easy"),
        ("What does 'CPU' stand for?", ["Central Processing Unit", "Computer Personal Unit", "Central Programming Unit", "Computer Processing Unit"], "a", "easy"),
        ("Which company makes the iPhone?", ["Google", "Samsung", "Apple", "Microsoft"], "c", "easy"),
        ("What does 'USB' stand for?", ["Universal Serial Bus", "Universal System Bus", "Universal Storage Bus", "Universal Service Bus"], "a", "easy"),
        ("Which programming language is used for web development?", ["Python", "Java", "HTML", "C++"], "c", "easy"),
        ("What is the name of Google's web browser?", ["Safari", "Firefox", "Edge", "Chrome"], "d", "easy"),
        ("Which social media platform is owned by Facebook?", ["Snapchat", "Instagram", "Twitter", "TikTok"], "b", "easy"),
        # Medium Questions
        ("What is the main language used for Android app development?", ["Swift", "Kotlin", "Java", "Python"], "c", "medium"),
        ("Which company developed the Linux operating system?", ["IBM", "Google", "Red Hat", "Linus Torvalds"], "d", "medium"),
        ("What does 'RAM' stand for?", ["Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Account Memory"], "a", "medium"),
        ("Which company developed the Windows operating system?", ["Apple", "Microsoft", "Google", "IBM"], "b", "medium"),
        ("Which programming language is primarily used for iOS app development?", ["Java", "Python", "Swift", "C++"], "c", "medium"),
        ("What does 'AI' stand for?", ["Artificial Intelligence", "Automatic Intelligence", "Advanced Intelligence", "Applied Intelligence"], "a", "medium"),
        ("Which company developed the Android operating system?", ["Apple", "Microsoft", "Google", "Samsung"], "c", "medium"),
        ("Which company is known for its search engine?", ["Apple", "Google", "Microsoft", "IBM"], "b", "medium"),
        ("What does 'SQL' stand for?", ["Standard Query Language", "Structured Query Language", "Sequential Query Language", "Simple Query Language"], "b", "medium"),
        ("Which company created the Java programming language?", ["Google", "Microsoft", "Apple", "Sun Microsystems"], "d", "medium"),
        # Hard Questions
        ("Who is known as the father of computers?", ["Steve Jobs", "Charles Babbage", "Alan Turing", "John von Neumann"], "b", "hard"),
        ("What was the first computer virus?", ["ILOVEYOU", "MyDoom", "Creeper", "Melissa"], "c", "hard"),
        ("Which programming language was developed by Guido van Rossum?", ["C++", "Python", "Java", "Ruby"], "b", "hard"),
        ("What does 'DNS' stand for?", ["Domain Name System", "Direct Name System", "Domain Network System", "Direct Network System"], "a", "hard"),
        ("Which company developed the first personal computer?", ["Apple", "IBM", "Microsoft", "Commodore"], "b", "hard"),
        ("What was the first web browser?", ["Internet Explorer", "Mosaic", "Netscape Navigator", "Opera"], "b", "hard"),
        ("Which company developed the C programming language?", ["Google", "Microsoft", "Apple", "Bell Labs"], "d", "hard"),
        ("What is the maximum value of an IP address?", ["255.255.255.255", "256.256.256.256", "127.127.127.127", "128.128.128.128"], "a", "hard"),
        ("What does 'BIOS' stand for?", ["Basic Input Output System", "Binary Input Output System", "Basic Integrated Output System", "Binary Integrated Output System"], "a", "hard"),
        ("Which programming language is used for data analysis and machine learning?", ["R", "HTML", "Swift", "JavaScript"], "a", "hard")
    ],
    "Art": [
        # Easy Questions
        ("Who painted the Mona Lisa?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "c", "easy"),
        ("Which artist is known for the painting 'Starry Night'?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], "c", "easy"),
        ("Which famous sculpture is found in Giza, Egypt?", ["Statue of Liberty", "Moai Statues", "The Thinker", "The Great Sphinx"], "d", "easy"),
        ("Which artist is famous for the 'Campbell's Soup Cans'?", ["Andy Warhol", "Roy Lichtenstein", "Keith Haring", "Jean-Michel Basquiat"], "a", "easy"),
        ("Which art movement is Salvador Dalí associated with?", ["Cubism", "Surrealism", "Impressionism", "Expressionism"], "b", "easy"),
        ("Which artist is known for the painting 'The Persistence of Memory'?", ["Pablo Picasso", "Salvador Dalí", "Claude Monet", "Edvard Munch"], "b", "easy"),
        ("Which building is a symbol of Paris, France?", ["Eiffel Tower", "Colosseum", "Statue of Liberty", "Big Ben"], "a", "easy"),
        ("Which artist painted 'The Last Supper'?", ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"], "c", "easy"),
        ("Which artist is known for the painting 'The Scream'?", ["Claude Monet", "Pablo Picasso", "Edvard Munch", "Vincent van Gogh"], "c", "easy"),
        ("Which museum is home to the Mona Lisa?", ["The British Museum", "The Louvre", "The Prado", "The Uffizi Gallery"], "b", "easy"),
        # Medium Questions
        ("Which artist is known for the painting 'Guernica'?", ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Leonardo da Vinci"], "b", "medium"),
        ("Which artist is famous for cutting off part of his own ear?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Claude Monet"], "c", "medium"),
        ("Which art movement did Claude Monet belong to?", ["Cubism", "Surrealism", "Impressionism", "Expressionism"], "c", "medium"),
        ("Who painted 'The Birth of Venus'?", ["Leonardo da Vinci", "Sandro Botticelli", "Michelangelo", "Raphael"], "b", "medium"),
        ("Which artist painted the ceiling of the Sistine Chapel?", ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"], "a", "medium"),
        ("Which artist is known for the painting 'Water Lilies'?", ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Salvador Dalí"], "c", "medium"),
        ("Which art movement is known for its use of geometric shapes?", ["Cubism", "Surrealism", "Impressionism", "Expressionism"], "a", "medium"),
        ("Who is the artist behind the 'Girl with a Pearl Earring'?", ["Jan Vermeer", "Rembrandt", "Peter Paul Rubens", "Frans Hals"], "a", "medium"),
        ("Which painting technique uses dots of color to create images?", ["Cubism", "Pointillism", "Impressionism", "Fauvism"], "b", "medium"),
        ("Which artist is known for the painting 'American Gothic'?", ["Edward Hopper", "Grant Wood", "Georgia O'Keeffe", "Jackson Pollock"], "b", "medium"),
        # Hard Questions
        ("Which artist painted the 'Nighthawks'?", ["Edward Hopper", "Grant Wood", "Georgia O'Keeffe", "Jackson Pollock"], "a", "hard"),
        ("Which artist is known for the 'Blue Period'?", ["Claude Monet", "Pablo Picasso", "Salvador Dalí", "Edvard Munch"], "b", "hard"),
        ("Which painting technique involves applying paint thickly?", ["Watercolor", "Impasto", "Glazing", "Underpainting"], "b", "hard"),
        ("Which artist created the sculpture 'The Thinker'?", ["Auguste Rodin", "Henry Moore", "Alexander Calder", "Constantin Brâncuși"], "a", "hard"),
        ("Which art movement is characterized by a focus on light and color?", ["Cubism", "Surrealism", "Impressionism", "Expressionism"], "c", "hard"),
        ("Who painted 'The Night Watch'?", ["Rembrandt", "Peter Paul Rubens", "Jan Vermeer", "Frans Hals"], "a", "hard"),
        ("Which artist is known for the painting 'Las Meninas'?", ["Francisco Goya", "Diego Velázquez", "El Greco", "Murillo"], "b", "hard"),
        ("Which artist is famous for the painting 'Liberty Leading the People'?", ["Eugène Delacroix", "Jacques-Louis David", "Jean-Auguste-Dominique Ingres", "Théodore Géricault"], "a", "hard"),
        ("Which artist is known for the 'Self-Portrait with Thorn Necklace and Hummingbird'?", ["Frida Kahlo", "Diego Rivera", "Pablo Picasso", "Salvador Dalí"], "a", "hard"),
        ("Who painted 'The Raft of the Medusa'?", ["Théodore Géricault", "Eugène Delacroix", "Jean-Auguste-Dominique Ingres", "Jacques-Louis David"], "a", "hard")
    ]
}