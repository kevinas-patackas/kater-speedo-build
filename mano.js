const mapping = {
  min: {
    reading: 0,
    value: 0,
  },
  max: {
    reading: 1000,
    value: 100,
  },
  ranges: [
    {
      reading: 200,
      value: 50,
    },
    {
      reading: 400,
      value: 90,
    },
    {
      reading: 300,
      value: 70
    }
  ]
};

const mappingSorted = {
  ...mapping,
  ranges: mapping.ranges.sort((a, b) => a.reading - b.reading)
}

function findValueByRange(reading) {
  const upperRangeIndex = mappingSorted.ranges.findIndex(range => range.reading > reading);
  const lowerRangeIndex = upperRangeIndex - 1;

  let upperRange = mappingSorted.ranges[upperRangeIndex];
  let lowerRange = mappingSorted.ranges[lowerRangeIndex];

  if (!upperRange) {
    upperRange = mappingSorted.max;
    lowerRange = mappingSorted.ranges[mappingSorted.ranges.length - 1];
  }

  if (!lowerRange) {
    lowerRange = mappingSorted.min;
  }

  const value = (reading - lowerRange.reading)/(upperRange.reading - lowerRange.reading) * (upperRange.value - lowerRange.value) + lowerRange.value;


  return Math.round(value);
}

console.log(findValueByRange(-100))
console.log(findValueByRange(0))
console.log(findValueByRange(100))
console.log(findValueByRange(250))
console.log(findValueByRange(350))
console.log(findValueByRange(400))
console.log(findValueByRange(450))
console.log(findValueByRange(600))
console.log(findValueByRange(1000))
console.log(findValueByRange(1100))
