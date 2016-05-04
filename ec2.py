def flattenTags(tags):
    """Flatten EC2 instance tags

    When using ``awscli`` or ``boto3``, a call to describe EC2
    instances will bundle the instances' tags like this:
    ``[{'Key': 'System', 'Value':'Ubuntu'}, {...}]``

    This function flattens it down to:
    ``{'system': 'ubuntu'}``

    Args:
        tags (list): List of dicts as {'Key': 'foo', 'Value': 'bar'}

    Returns:
        A dict mapping the value of 'Value' to the value of 'Key'
        (see example in description)
        """
    return {tag['Key'].lower(): tag['Value'].lower() for tag in tags}
