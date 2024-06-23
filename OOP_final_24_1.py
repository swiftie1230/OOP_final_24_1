import streamlit as st
import pandas as pd

exam_title = "2024 Objective Oriented Programming Final"
fname = "OOP_Final_Grading.xlsx"
solution_1 = '''Solution
1. (10p - 2p each) \n
(a) T \n
(b) T \n
(c) F \n
(d) F \n
(e) T \n
'''

solution_2 = '''
2. (8p - 2p each) \n
(a) Downcasting \n 
(b) Method Overriding \n
(c) Wrapper \n
(d) Module \n
'''

solution_3 = '''
3. (15p) \n
(a) - 3p \n
c:\windows \n
(b) - 3p \n
5 \n
(c) - 6p (2p each) \n
new Student() ->	Person Student  \n
new Researcher() ->	Person Researcher  \n
new Professor() ->	Person Researcher Professor  \n
 \n
deducted 1 point for minor mistakes. (ex. arrows) \n
'''

solution_4 = '''
4. (10p) \n
(a) - 5p \n
If the purpose is properly described and the content is appropriate, 5 points; otherwise, 0 points. \n
(b) - 5p \n
If static binding is mentioned for overloading and dynamic binding for overriding, 5 points; otherwise, 0 points. \n
'''

solution_5_1 = '''
5. (8P) 
'''

code_5_1 = '''
// (1) TODO
if (x > 0 && y > 0) { 
super.move(x, y); 
} else { return; }
'''

code_5_2 = '''
// (2) TODO
public String toString() { 
return "(" + getX() + "," + getY() + ") point"; 
}
'''

solution_5_2 = '''

(1) TODO - 5p \n
(2) TODO - 3p \n
deducted 1 point for minor mistakes \n
'''

solution_6_1 = '''
6. (12p)
(a) - 3p \n
new Dog(); \n
(b) - 3p \n
new Cat(); \n
(c) - 3p \n
Dog dog = (Dog) animals[i];  \n
(d) - 3p \n
Cat cat = (Cat) animals[i];  \n
'''

solution_6_2 ='''

deducted 1 point for minor mistakes, such as not using a semicolon. \n
'''

solution_7_1 = '''
7. (10p) \n
'''

code_7 ='''
import java.io.*;
public class FileReadHangulSuccess {
    public static void main(String[] args) {
        InputStreamReader in = null;
        FileInputStream fin = null;
        try {
            fin = new FileInputStream("c:\\temp\\hangul.txt");
            in = new InputStreamReader(fin, "UTF-8"); -> 1p
            int c;
            System.out.println("Encoding character set : " + in.getEncoding());
            while ((c = in.read()) != -1) {
                System.out.print((char)c);
            }
            in.close();
            fin.close();
        } catch (IOException e) {
            System.out.println("IO error");
        }
    }
}

'''

solution_7_2 = '''
InputStreamReader, FileInputStream Declaration - 1p \n
InputStreamReader, FileInputStream Definition & Initialization - 3p (deducted 1 point for mistakes) \n 
while statement - 3p \n
Appropriately closed InputStreamReader, FileInputStream - 3p  \n
'''

solution_8 = '''
8. (10p) \n
(a) - 4p (deducted 2 points if the explanation was insufficient) \n 
In Java, a byte stream (e.g., InputStream and OutputStream) handles raw binary data and is typically used for handling files like images or videos, whereas a character stream (e.g., Reader and Writer) deals with character data and is used for text files, ensuring proper encoding and decoding of characters \n
(b) (A), (C) - 3p \n
(c) - 3p \n
'''

solution_9 = '''
9. (9p - each 3p) \n
(1): new StringTokenizer(s, "/"); \n                                                            
(2): st.hasMoreTokens() \n                                                                              
(3): st.nextToken() \n
\n
deducted 1 point for minor mistakes, such as not using a semicolon. \n
'''

solution_10_1 = '''
10. (11p)
'''

code_10 ='''
import java.util.HashMap;
import java.util.Scanner;
public class StudentGrades {
    public static void main(String[] args) {
        HashMap<String, Double> students = new HashMap<>();
        Scanner scanner = new Scanner(System.in);
        while (true) {   // Reading student names and grades
            System.out.println("Enter student name and grade (or type \"end\" to finish):");
            String input = scanner.nextLine();
            if (input.equals("end")) {
                break;
            }
            String[] parts = input.split(" ");
            String name = parts[0];
            double grade = Double.parseDouble(parts[1]);
            students.put(name, grade);
        }
        while (true) {         // Continuously reading student's name to find the grade until "end" is entered
            System.out.println("Enter the student's name to find the grade (or type \"end\" to finish):");
            String studentName = scanner.nextLine();
            if (studentName.equals("end")) {
                break;
            }
            if (students.containsKey(studentName)) {
                System.out.println("Grade of " + studentName + ": " + students.get(studentName));
            } else {
                System.out.println("Student not found.");
            }
        }
        scanner.close();
    }
}

'''

solution_10_2 = '''

Reading student names and grades - 5p (deducted 1 point if the put function was incorrectly written as add)  \n
Continuously reading student's name to find the grade until "end" is entered - 5p (deducted 1 point for not handling exceptions) \n
If you wrote any code that is right, we gave 1 point \n 
'''

# Setup Title & Wide layout
st.set_page_config(page_title=exam_title, layout="wide")
st.markdown(
    """
    <style>
    textarea {
        font-size: 2rem !important;
    }
    input {
        font-size:1.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Load the Excel data
df = pd.read_excel(fname)

def get_student_data(student_id):
    """
    Fetch the data for a given student ID from the Excel file.
    
    Args:
    - student_id (int): The ID of the student.
    
    Returns:
    - pd.DataFrame or None: The data for the student if found, otherwise None.
    """
    student_data = df[df["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None

# Streamlit app layout and logic
st.title(exam_title)

# Get the student ID from the user
student_id = st.text_input("Enter your email", value='hwanheelee@cau.ac.kr')

# When the user provides a student ID, fetch and display the data
if student_id:
    data = get_student_data(student_id)
    
    if data is not None:
        to_show = data.set_index("e-mail")
        st.write("E-mail: ", to_show.index[0])
        s = to_show.style.format({"Expense": lambda x : '{:.4f}'.format(x)})
        st.dataframe(s, hide_index=True)
    else:
        st.write(f"No data found for email: {student_id}")
        
st.write(solution_1)  
st.markdown("""---""")
st.write(solution_2)  
st.markdown("""---""")
st.write(solution_3)  
st.markdown("""---""")
st.write(solution_4)  
st.markdown("""---""")
st.write(solution_5_1)  
st.code(code_5_1, language='java')
st.code(code_5_2, language='java')
st.write(solution_5_2)  
st.markdown("""---""")
st.write(solution_6_1)  
st.write(solution_6_2)  
st.markdown("""---""")
st.write(solution_7_1) 
st.code(code_7, language='java')
st.write(solution_7_2) 
st.markdown("""---""")
st.write(solution_8) 
st.markdown("""---""")
st.write(solution_9) 
st.markdown("""---""")
st.write(solution_10_1) 
st.code(code_10, language='java')
st.write(solution_10_2)  
        
