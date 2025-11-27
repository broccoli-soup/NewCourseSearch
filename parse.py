fullText = """CAS CS 108: Programming for Non-CS Majors
A rigorous introduction to programming for students not majoring in computer science. Covers a broad set of topics about application development, including basic programming concepts, testing and debugging, abstraction and design, and an introduction to data analytics. Effective Fall 2018, this course fulfills a single unit in the following BU Hub area: Quantitative Reasoning I.
BU Hub Learn More
 CAS CS 111: Introduction to Computer Science 1
The first course for computer science majors and anyone seeking a rigorous introduction. Develops computational problem-solving skills by programming in the Python language, and exposes students to variety of other topics from computer science and its applications. Carries MCS divisional credit in CAS. Effective Fall 2018, this course fulfills a single unit in each of the following BU Hub areas: Quantitative Reasoning II, Creativity/Innovation, Critical Thinking.
BU Hub Learn More
 CAS CS 112: Introduction to Computer Science 2
Undergraduate Prerequisites: (CASCS111) or equivalent. - Covers advanced programming techniques and data structures. Topics include recursion, algorithm analysis, linked lists, stacks, queues, trees, graphs, tables, searching, and sorting. Carries MCS divisional credit in CAS. Effective Fall 2018, this course fulfills a single unit in the following BU Hub areas: Quantitative Reasoning II, Creativity/Innovation, Critical Thinking.
BU Hub Learn More
 CAS CS 115: Academic Writing in Computer Science
Undergraduate Prerequisites: CAS WR 120 or equivalent; CAS CS 111. - Pre-req: WR 120 or equivalent, CS 111. This 2-credit course offers a Writing Intensive unit through the topic of computer science. Students engage with readings and discussions in current computer science issues. The course focuses on teaching critical reading, creating a strong argument, and engaging with a variety of sources. Effective Spring 2023, this course fulfills a single unit in the following BU Hub area: Writing-Intensive Course.
BU Hub Learn More
 CAS CS 131: Combinatoric Structures
Fundamentals of logic (the laws of logic, rules of inference, quantifiers, proofs and inductive reasoning), fundamental principles of counting (permutations, combinations), set theory, relations and functions, principles for manipulating basic combinatoric structures. Effective Fall 2018, this course fulfills a single unit in the following BU Hub area: Quantitative Reasoning II. Effective Fall 2019, this course fulfills a single unit in each of the following BU Hub areas: Quantitative Reasoning II, Critical Thinking.
BU Hub Learn More
 CAS CS 132: Geometric Algorithms
Undergraduate Prerequisites: (CASCS111 & CASMA123) - Basic concepts, data structures, and algorithms for geometric objects. Examples of topics: Cartesian geometry, transformations and their representation, queries and sampling, triangulations. Emphasis on rigorous reasoning and analysis, advancing algorithmic maturity and expertise in its application. Effective Fall 2019, this course fulfills a single unit in the following BU Hub areas: Quantitative Reasoning II, Digital/Multimedia Expression.
BU Hub Learn More
 CAS CS 210: Computer Systems
Undergraduate Prerequisites: (CASCS112) - Fundamental concepts of computer systems and systems programming. Hardware fundamentals including digital logic, memory systems, processor design, buses, I/O subsystems, data representations, computer arithmetic, and instruction- set architecture. Software concepts including assembly language programming, operating systems, assemblers, linkers, and systems programming in C. Effective Fall 2018, this course fulfills a single unit in the following BU Hub area: Quantitative Reasoning II.
BU Hub Learn More
 CAS CS 235: Algebraic Algorithms
Undergraduate Corequisites: CASCS132 recommended. - Basic concepts and algorithms for manipulation of algebraic objects, such as residues, matrices, polynomials; and applications to various CS areas, such as cryptography and fault-tolerance. Emphasis on rigorous reasoning and analysis. Effective Fall 2018, this course fulfills a single unit in the following BU Hub area: Quantitative Reasoning II.
BU Hub Learn More
 CAS CS 237: Probability in Computing
Undergraduate Prerequisites: (CASCS131) - Introduction to basic probabilistic concepts and methods used in computer science. Develops an understanding of the crucial role played by randomness in computing, both as a powerful tool and as a challenge to confront and analyze. Emphasis on rigorous reasoning, analysis, and algorithmic thinking. Effective Fall 2018, this course fulfills a single unit in each of the following BU Hub areas: Quantitative Reasoning II, Critical Thinking.
BU Hub Learn More"""

courseChunks = fullText.split('CAS CS ')[1:]  # Skip empty first part
courseList = ['CAS CS ' + chunk.strip() for chunk in courseChunks]

for course in courseList:
    lines = course.split(".", "-")
    code_title = lines[0].strip()[0:10]
    prereq_line = "None listed"
    
    for line in lines:
        if "Undergraduate Prerequisites:" in line:
            start = line.find("Undergraduate Prerequisites:") + len("Undergraduate Prerequisites:")
            prereq_line = line[start:].strip()
            break  # stop after finding first prerequisites line
        elif "Undergraduate Corequisites:" in line:
            start = line.find("Undergraduate Corequisites:") + len("Undergraduate Corequisites:")
            prereq_line = line[start:].strip()
            break

    print(f"{code_title} Prerequisites: {prereq_line}\n")