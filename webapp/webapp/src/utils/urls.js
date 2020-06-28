const reverseUrl = (urlName, ...params) => {
    return DJ_CONST.reverse[urlName](...params);
};

export default reverseUrl;
