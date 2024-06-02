export default function getStudentIdsSum(students) {
  return students.reduce((accum, current) => accum + current.id, 0);
}
