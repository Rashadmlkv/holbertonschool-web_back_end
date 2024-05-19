/* eslint-disable */
export default class Currency {
    constructor(code, name) {
        this._code = code
        this._name = name
    } 

    get code() {
        return this._code;
    }
    
    set code(newCode) {
        if (typeof newCode !== 'string') throw TypeError('Code must be  a String');
        this._code = newCode;
    }

    get name() {
        return this._name;
    }
    set name(newName) {
        if (typeof newName !== 'string') throw TypeError('Name must be a String');
        this._code = newName
    }

    displayFullCurrency() {
        return `${this._name} (${this._code})`;
    }
}