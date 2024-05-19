/* eslint-disable */
import ClassRoom from "./0-classroom.js";
const initializeRooms = () => {
    const rooms = [
        new ClassRoom(19),
        new ClassRoom(20),
        new ClassRoom(34)
    ];
    return rooms;
};
export default initializeRooms;