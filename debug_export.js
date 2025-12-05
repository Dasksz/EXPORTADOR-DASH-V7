const XLSX = { utils: { book_new: () => ({}), aoa_to_sheet: () => ({}), book_append_sheet: () => {}, encode_col: (i) => 'C' + i } };

// Mock Data
const quarterMonths = [{ key: '1', label: 'M1' }, { key: '2', label: 'M2' }, { key: '3', label: 'M3' }];
const monthsCount = quarterMonths.length;

const svColumns = [
    { id: 'total_elma', label: 'TOTAL ELMA', type: 'standard', isAgg: true },
    { id: '707', label: 'EXTRUSADOS', type: 'standard' },
    { id: 'tonelada_elma', label: 'TONELADA ELMA', type: 'tonnage', isAgg: true },
    { id: 'total_foods', label: 'TOTAL FOODS', type: 'standard', isAgg: true },
    { id: 'tonelada_foods', label: 'TONELADA FOODS', type: 'tonnage', isAgg: true },
    { id: 'geral', label: 'GERAL', type: 'geral', isAgg: true },
    { id: 'pedev', label: 'PEDEV', type: 'pedev', isAgg: true }
];

let colIdx = 2;
const colMap = {};

svColumns.forEach(col => {
    colMap[col.id] = colIdx;
    let span = 0;
    if (col.type === 'standard') span = monthsCount + 1 + 4;
    else if (col.type === 'tonnage') span = 3;
    else if (col.type === 'geral') span = 4;
    else if (col.type === 'pedev') span = 1;
    colIdx += span;
});

console.log('ColMap:', colMap);

// Simulate Geral Formula
const elmaIdx = colMap['total_elma'];
const foodsIdx = colMap['total_foods'];
const excelRow = 5;
const getColLet = (idx) => 'C' + idx; // Mock

const fFat = `${getColLet(elmaIdx + monthsCount + 1)}${excelRow}+${getColLet(foodsIdx + monthsCount + 1)}${excelRow}`;
console.log('Formula Fat:', fFat);
console.log('Expected Elma MetaFat Index:', elmaIdx + monthsCount + 1);

// Simulate Data Row Push
const d = { avgFat: 100, metaFat: 200, metaPos: 10 };
console.log('Geral AvgFat Value:', d.avgFat);
