/* eslint-disable */
export default function appendToEachArrayValue(array, appendString) {
	  for (let el of array) {
		      const idx = array.indexOf(el);
		      array[idx] = appendString + el;
		    }

	  return array;
}
