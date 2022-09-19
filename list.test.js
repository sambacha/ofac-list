import data, { nestedArray } from "./fixture";
import packageJson from "./package.json";
it("should have to correct values", () => {
	expect(data.nested.key).toBe("value");
});

it("should be able to write properties", () => {
	// known key
	data.nested.key2 = "new value";
	expect(data.nested.key2).toBe("new value");
	// unknown key
	data.nested.key3 = "value3";
	expect(data.nested.key3).toBe("value3");
	// array methods and prototype properties
	data.nested.array.push(4);
	expect(data.nested.array.length).toEqual(4);
	// direct and nested access
	const a = data.nested.array2;
	data.nested.array2[1] = 42;
	expect(a[1]).toEqual(42);
	expect(a.length).toEqual(3);
	// only nested access
	expect(data.nested.array3[1]).toBe("ok");
	expect(data.nested.array4[10]).toBe("ok");
	expect(data.nested.array5[0]).toBe("ok");
	// object methods
	expect(data.nested.object.hasOwnProperty("test")).toBe(true);
	// unknown object property
	data.nested.object2.unknownProperty = 42;
	expect(data.nested.object2.unknownProperty).toBe(42);
	data.nested.object3.unknownProperty = { deep: "deep" };
	expect(data.nested.object3.unknownProperty.deep).toBe("deep");
    expect(content).toMatch(/\.unknownProperty\s*=/);
	expect(content).toMatch(/\.unknownProperty\.deep\)/);
	expect(content).not.toMatch(/\\?"dependencies\\?"/);
	expect(content).not.toMatch(/\\?"scripts\\?"/);
});