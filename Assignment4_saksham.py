def read_feedbackF(fnames):
    feedback_data = []
    for file_name in fnames:
        try:
            with open(file_name, 'r') as file:
                feedback_data.extend(file.readlines())
        except FileNotFoundError:
            print(f"Error: {file_name} not found.")
    return feedback_data

def parse_feedback(feedback_data):
    parse_feedback = []
    overallRating = 0
    for feedback in feedback_data: 
        try:
            name, rate = feedback.split(':')
            rating, comment = rate.split(' - ')
            rating = int(rating.strip())
            parse_feedback.append((name.strip(), rating, comment.strip()))
            overallRating += rating
        except ValueError:
            print(f"Error: Unable to parse feedback line: {feedback}")
    
    average_rating = overallRating / len(parse_feedback) if parse_feedback else 0
    return parse_feedback, average_rating

def write_summary(parsed_feedback, average_rating, summary_file):
    try:
        with open(summary_file, 'w') as file:
            file.write(f"Total Feedback Entries: {len(parsed_feedback)}\n")
            file.write(f"Average Rating: {average_rating:.2f}\n\n")
            file.write("Feedbacks:\n")
            for name, rating, comment in parsed_feedback:
                file.write(f"{name}: {rating} - {comment}\n")
    except IOError:
        print(f"Error: Could not write to file {summary_file}")

def main():
    feedback_files = ['feedback1.txt', 'feedback2.txt', 'feedback3.txt']
    feedback_data = read_feedbackF(feedback_files)
    parsed_feedback, average_rating = parse_feedback(feedback_data)
    write_summary(parsed_feedback, average_rating, 'feedback_summary.txt')

if __name__ == "__main__":
    main()
