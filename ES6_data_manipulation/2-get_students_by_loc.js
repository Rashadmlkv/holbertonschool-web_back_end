export default function getStudentsByLocation(students, place) {
  return students.filter(({ location }) => location === place);
}
