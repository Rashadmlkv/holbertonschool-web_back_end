export default function createInt8TypedArray(length, position, value) {
  const arr = new Int8Array(length);

  if (position >= length || position < 0) throw new Error('Position outside range');

  arr[position] = value;

  const dataView = new DataView(arr.buffer);

  return dataView;
}
