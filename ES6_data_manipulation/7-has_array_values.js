export default function hasValuesFromArray(set, array) {
  for (let index = 0; index < array.length; index += 1) {
    const element = array[index];
    if (!set.has(element)) return false;
  }

  return true;
}
