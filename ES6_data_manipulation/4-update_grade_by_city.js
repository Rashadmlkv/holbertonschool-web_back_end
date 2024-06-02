export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter(({ location }) => location === city)
    .map((student) => {
      const grade = newGrades.filter(({ studentId }) => studentId === student.id)[0];
      return {
        ...student,
        grade: grade ? grade.grade : 'N/A',
      };
    });
}
