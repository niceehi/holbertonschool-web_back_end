export default function getListStudentsIds(obj) {
  if (!Array.isArray(obj)) {
    return [];
  }

  return obj.map((student) => student.id);
}
